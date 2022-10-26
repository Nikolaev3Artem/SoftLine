// функция вызова окна
function show_popap(id_popap) {
    var id = "#" + id_popap;
    $(id).addClass('active');
  }
   
  // функция закрытия окна 
  $(".close_popap").click( function(){
    $(".overlay").removeClass("active");
  });

  let i = 1;
  for(let li of carousel.querySelectorAll('li')) {
    li.style.position = 'relative';
    li.insertAdjacentHTML('beforeend', `<span style="position:absolute;left:0;top:0">${i}</span>`);
    i++;
  }
