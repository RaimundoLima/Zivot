d = new Date();
iniciarCalendario(d.getDay(),d.getDate(),d.getMonth(),d.getFullYear(),$("#mes-calendario"),$("#dias-calendario"));

//https://idangero.us/swiper/get-started/
var outrasOpcoes = new Swiper ('.swiper-container', {
    direction: 'horizontal',
    loop: false,

    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

})