//ABA PERFIL
function modalAgendamento(horaInicio,horaTermino,dia,mes,ano){
    //AJAX
    //modificar modal
    /*
    $('#detalhe-data').html($('#dia-selecionado').attr('data-data'));
    $('#detalhes-horario').html();    
    */
}

//ABA PAINEL
//TIPO É SE É PROFFISIONAL OU PACIENTE
function modalDetalhesConsulta(idConsulta, tipo){

    if(tipo == 'paciente'){
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
        $('#remarcarConsulta-modal').click(function(){iniciarCalendario($(this).attr('data-diaSemana'),parseInt($(this).attr('data-dia')),parseInt($(this).attr('data-mes')),parseInt($(this).attr('data-ano')),$("#mes-calendario"),$("#dias-calendario"))})
        $('#cancelarConsulta-modal').click(function(){});
        preencher botao de remarcar com dados da data, ano dia da semana etc
        */
    }else if(tipo == 'profissional'){
        /*
        $('#detalhes-paciente').html();
        $('#detalhe-data').html();
        $('#detalhes-horario').html();
        $('#detalhes-local').html();

        $('#remarcarConsulta-modal').off();
        $('#cancelarConsulta-modal').off();
        $('#remarcarConsulta-modal').click(function(){iniciarCalendario($(this).attr('data-diaSemana'),parseInt($(this).attr('data-dia')),parseInt($(this).attr('data-mes')),parseInt($(this).attr('data-ano')),$("#mes-calendario"),$("#dias-calendario"))})
        $('#cancelarConsulta-modal').click(function(){});
        preencher botao de remarcar com dados da data, ano dia da semana etc
        */
    }
}

$('#fechar-detalhesConsulta').click(function(){
    $('#remarcarConsulta-modal').off("click");
    $('#cancelarConsulta-modal').off("click");
});


//COLOCAR NO FOR QUE APARECE DAS CONSULTAS NO PAINEL DE PACIENTE OU PROFISSIONAL
$('#remarcarConsulta-modal').click(function(){iniciarCalendario($(this).attr('data-diaSemana'),parseInt($(this).attr('data-dia')),
parseInt($(this).attr('data-mes')),parseInt($(this).attr('data-ano')),$("#mes-calendario"),$("#dias-calendario"))})

