// Shared site behaviour
(function(){
  var btn=document.querySelector('.menu-btn'), nav=document.querySelector('.nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o)})}
  // Print buttons: fall back gracefully where printing is blocked
  document.querySelectorAll('[data-print]').forEach(function(b){
    b.addEventListener('click',function(){
      try{window.print()}catch(e){}
      var n=document.getElementById('print-note'); if(n){n.hidden=false}
    });
  });
  var y=document.getElementById('year'); if(y){y.textContent=new Date().getFullYear()}
})();
