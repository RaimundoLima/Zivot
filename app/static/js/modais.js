//ABA PERFIL
function modalAgendamento(idConsulta){
    //AJAX
    //modificar modal
    /*
    $('#detalhes-proffissional').html();
    $('#detalhes-especialidade').html();
    $('#detalhe-data').html($('#dia-selecionado').attr('data-data'));
    $('#detalhes-horario').html();
    $('#detalhes-valor').html();
    
    */
}

//ABA PAINEL
function modalDetalhesConsulta(idConsulta){
    //AJAX
    //modificar modal
    /*
    $('#detalhes-proffissional').html();
    $('#detalhes-especialidade').html();
    $('#detalhe-data').html();
    $('#detalhes-horario').html();
    $('#detalhes-local').html();

    $('#remarcarConsulta-modal').off();
    $('#cancelarConsulta-modal').off();
    $('#remarcarConsulta-modal').click(function(){});
    $('#cancelarConsulta-modal').click(function(){});
    preencher botao de remarcar com dados da data, ano dia da semana etc
    */
}

$('#fechar-detalhesConsulta').click(function(){
    $('#remarcarConsulta-modal').off("click");
    $('#cancelarConsulta-modal').off("click");
});

$('#remarcarConsulta-modal').click(function(){iniciarCalendario($('#remarcarConsulta-modal').attr('data-diaSemana'),
$('#remarcarConsulta-modal').attr('data-dia'),
$('#remarcarConsulta-modal').attr('data-mes'),
$('#remarcarConsulta-modal').attr('data-ano'))})

