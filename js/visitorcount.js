const hitCount = document.getElementById('count');

updateHitCount();

function updateHitCount() {
  fetch('https://f4fue6j779.execute-api.us-east-1.amazonaws.com/HitCounter')
  .then(response => response.json())
  .then(response => {
    hitCount.innerHTML = response.visitcount;
  });
}
