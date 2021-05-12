// Store value in local browser so that value will be remembered even when refreshed
if (!localStorage.getItem('counter')) {
  localStorage.setItem('counter', 0);
}

function count() {
  let counter = localStorage.getItem('counter');
  counter++;
  document.querySelector('h1').innerHTML = counter;
  localStorage.setItem('counter', counter);

//   if (counter % 10 === 0) {
//     alert(`Counter is now ${counter}`);
//   }
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('h1').innerHTML = localStorage.getItem('counter');
  document.querySelector('button').onclick = count;

  // Run the count() function every 1 second
  // setInterval(count, 1000);
});