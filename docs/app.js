const pw = document.getElementById('pw');
const bar = document.getElementById('bar');
const strength = document.getElementById('strength');
const score = document.getElementById('score');
const entropy = document.getElementById('entropy');
const feedback = document.getElementById('feedback');

// ✅ Use live backend instead of localhost
const API_URL = "https://password-strength-checker-1inv.onrender.com/evaluate";

async function evaluate(p) {
  const res = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password: p })
  });

  if (!res.ok) throw new Error('API not reachable.');
  return await res.json();
}

let timer;
pw.addEventListener('input', () => {
  clearTimeout(timer);
  const val = pw.value;
  timer = setTimeout(async () => {
    if (!val) {
      bar.style.width = '0%';
      strength.textContent = '—';
      score.textContent = 'score: —';
      entropy.textContent = 'entropy: — bits';
      feedback.innerHTML = '';
      return;
    }
    try {
      const data = await evaluate(val);
      const pct = data.score;
      bar.style.width = pct + '%';
      strength.textContent = data.strength;
      score.textContent = 'score: ' + data.score;
      entropy.textContent = 'entropy: ' + data.entropy_bits_adjusted.toFixed(2) + ' bits';
      feedback.innerHTML = data.feedback.map(x => `<li>${x}</li>`).join('');
    } catch (_e) {
      strength.textContent = 'API offline';
      bar.style.width = '0%';
    }
  }, 250);
});
