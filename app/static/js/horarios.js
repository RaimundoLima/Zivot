d = new Date();

$('#AdicionarCompromisso-modal').click(function(){iniciarCalendario(d.getDay(),d.getDate(),d.getMonth(),d.getFullYear(),$("#mes-calendario"),$("#dias-calendario"))})

$('#HorarioExtra-modal').click(function(){iniciarCalendario(d.getDay(),d.getDate(),d.getMonth(),d.getFullYear(),$("#mes-calendario1"),$("#dias-calendario1"))})

$('#definirDomingo').click(function(){$('#dia-da-semana').html($(this).attr('data-dia'))});
$('#definirSegunda').click(function(){$('#dia-da-semana').html($(this).attr('data-dia'))});
$('#definirTerca').click(function(){$('#dia-da-semana').html($(this).attr('data-dia'))});
$('#definirQuarta').click(function(){$('#dia-da-semana').html($(this).attr('data-dia'))});
$('#definirQuinta').click(function(){$('#dia-da-semana').html($(this).attr('data-dia'))});
$('#definirSexta').click(function(){$('#dia-da-semana').html($(this).attr('data-dia'))});
$('#definirSabado').click(function(){$('#dia-da-semana').html($(this).attr('data-dia'))});

$('#modalDefinirHorario').on('hidden.bs.modal', function () {
    $('#horarios-atuais').empty();
    $('#hora-inicio option:first').prop('selected',true);
    $('#minuto-inicio option:first').prop('selected',true);
    $('#hora-final option:first').prop('selected',true);
    $('#minuto-final option:first').prop('selected',true);
});

$('#modalAdicionarCompromisso').on('hidden.bs.modal', function () {
    ano = d.getFullYear();
    $("#dias-calendario").empty();
});

$('#modalHorarioExtra').on('hidden.bs.modal', function () {
    ano = d.getFullYear();
    $("#dias-calendario1").empty();
    $('#horarios-atuais').empty();
    $('#hora-inicioExtra option:first').prop('selected',true);
    $('#minuto-inicioExtra option:first').prop('selected',true);
    $('#hora-finalExtra option:first').prop('selected',true);
    $('#minuto-finalExtra option:first').prop('selected',true);
});
