//COLOCAR NO FOR DA CRIAÇÃO DE CONSULTA
//$('#remarcarConsulta-modal').click(function(){iniciarCalendario($(this).attr('data-diaSemana'),parseInt($(this).attr('data-dia')),
//parseInt($(this).attr('data-mes')),parseInt($(this).attr('data-ano')),$("#mes-calendario"),$("#dias-calendario"))})

$(document).ready(function(){
    $('.rating').addRating({
        icon : 'star',
        max : 5,
        fieldName : 'rating',
        fieldId : 'nota'
    });
})
