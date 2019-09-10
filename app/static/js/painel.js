/* 
//Construção de consulta
consulta = $(document.createElement('div'));
consulta.addClass('consulta-marcada');

profissional = $(document.createElement('span'));
profissional.addClass('profissional-consulta');
profissional.html(VEM DO AJAX)

horario = $(document.createElement('span'));
horario.addClass('horario-consulta');
horario.html(horarioInicial+"-"+horarioFinal)

icon = $(document.createElement('i'));
icon.addClass('material-icons');
icon.html('date_range');
icon.attr('data-consulta', ID VINDO DO AJAX);
icon.click(function(){modalDetalhesConsulta(icon.attr('data-consulta'), //COLOCAR TIPO DO USUARIO);})

consulta.append(profissional);
consulta.append(horario);
consulta.append(icon);

$('#proximas-consultas').append(consulta);
*/

var buscaResultados = new Swiper ('.swiper-container', {
    direction: 'horizontal',
    loop: false,

    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

})