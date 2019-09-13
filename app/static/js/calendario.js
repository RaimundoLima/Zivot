meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"];
diasmeses = [31,28,31,30,31,30,31,31,30,31,30,31];
diassemana = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]
diasabrev = ["DOM ","SEG ","TER ","QUA ","QUI ","SEX ","SAB "]
d = new Date();
atual = d.getMonth();
diaInicial = 0;
diaFinal = 0;
ano = d.getFullYear();

function iniciarCalendario(diasemana,dia,mes,anoatual,mesDiv,diasDiv){
    atual = mes;
    ano = anoatual;
    éBissexto(ano);

    mesDiv.html(meses[mes]+"/"+ano);

    var diaInicial = diasemana;
    for(aux = dia; aux > 1; aux--){
        diaInicial--;        
        if(diaInicial == -1) diaInicial = 6;
    }

    if(diaInicial == 0){
        diaFinalMesPassado = 6;
    }else{
        diaFinalMesPassado = diaInicial-1;
    }
    
    diaFinal = diaInicial;
    for(aux = 1; aux < diasmeses[mes]; aux++){
        diaFinal = (diaFinal+1)%7;
    }
    gerarCalendario(diaInicial,atual,ano,diasDiv);
}

function éBissexto(ano){
    if(ano % 4 == 0 && ano % 100 != 0){
        diasmeses[1] = 29;
        return true;
    }else{
        if(ano % 4 != 0 && ano % 400 == 0){
            diasmeses[1] = 29;
            return true;
        }else{
            diasmeses[1] = 28;
            return false;
        }
    }
}

function gerarCalendario(diaInicial,atual,ano,diasDiv){
    diasDiv.empty();
    aux1 = atual-1;
    if(aux1 == -1) aux1 = 11;
    var diaMesAnt = diasmeses[aux1]-diaFinalMesPassado;
    var diaAtual = 1;
    diaProx = 1;
    contSemana = 0;    
    éBissexto(ano);
    tr = $(document.createElement('tr'));
    for(aux = 0; aux <= diaInicial-1; aux++){
        contSemana++;
        td = $(document.createElement('td')).html(diaMesAnt);
        aux6 = atual
        if(atual == 0) aux6 = 12;
        construirDia(td, contSemana-1, diaMesAnt, aux6, ano);
        tr.append(td);
        diaMesAnt++;
    }
    for(aux2 = contSemana; aux2 < 7; aux2++){
        contSemana++;
        td = $(document.createElement('td')).html(diaAtual);
        construirDia(td, contSemana-1, diaAtual, atual+1, ano);
        diaAtual++;
        tr.append(td);
    }
    diasDiv.append(tr);
    cont = Math.ceil((diasmeses[atual] - (diaAtual-1))/7);
    for(aux3 = 0;aux3 < cont;aux3++){
        aux5 = 0;
        tr = $(document.createElement('tr'));            
        for(aux4 = 0; aux4 < 7; aux4++){
            if(diaAtual <= diasmeses[atual]){
                dia = diaAtual;
            }else{
                dia = diaProx;
                diaProx++;
                aux5 = 1;
            }
            td = $(document.createElement('td')).html(dia);
            aux5 == 1 ? construirDia(td, aux4, dia, atual+2, ano) : construirDia(td, aux4, dia, atual+1, ano);
            diaAtual++;
            tr.append(td);
        }
        diasDiv.append(tr);
    }
}

$("#btn-left-calendario").click(function(){
    atual = atual-1;
    if(atual == -1){
        atual = 11;
        ano--;
    }
    éBissexto(ano);
    $("#mes-calendario").html(meses[atual]+"/"+ano);
    diaFinal = diaFinalMesPassado;
    diaInicial = diaFinalMesPassado;
    for(aux = diasmeses[atual]; aux > 1; aux--){
        diaInicial = diaInicial-1;
        if(diaInicial == -1){
            diaInicial = 6;
        }
    }
    if(diaInicial == 0){
        diaFinalMesPassado = 6;
    }else{
        diaFinalMesPassado = diaInicial-1;
    }
    gerarCalendario(diaInicial,atual,ano,$("#dias-calendario"));
});

$("#btn-right-calendario").click(function(){
    if(atual == 11) ano++;
    éBissexto(ano);
    atual = (atual + 1)%12;
    $("#mes-calendario").html(meses[atual]+"/"+ano);
    diaInicial = (diaFinal+1)%7;
    if(diaInicial == 0){
        diaFinalMesPassado = 6;
    }else{
        diaFinalMesPassado = diaInicial-1;
    }
    diaFinal = diaInicial;
    for(aux = 1; aux < diasmeses[atual]; aux++){
        diaFinal = (diaFinal+1)%7;
    }
    gerarCalendario(diaInicial,atual,ano,$("#dias-calendario"));
});

$("#btn-left-calendario1").click(function(){
    atual = atual-1;
    if(atual == -1){
        atual = 11;
        ano--;
    }
    éBissexto(ano);
    $("#mes-calendario1").html(meses[atual]+"/"+ano);
    diaFinal = diaFinalMesPassado;
    diaInicial = diaFinalMesPassado;
    for(aux = diasmeses[atual]; aux > 1; aux--){
        diaInicial = diaInicial-1;
        if(diaInicial == -1){
            diaInicial = 6;
        }
    }
    if(diaInicial == 0){
        diaFinalMesPassado = 6;
    }else{
        diaFinalMesPassado = diaInicial-1;
    }
    gerarCalendario(diaInicial,atual,ano,$("#dias-calendario1"));
});

$("#btn-right-calendario1").click(function(){
    if(atual == 11) ano++;
    éBissexto(ano);
    atual = (atual + 1)%12;
    $("#mes-calendario1").html(meses[atual]+"/"+ano);
    diaInicial = (diaFinal+1)%7;
    if(diaInicial == 0){
        diaFinalMesPassado = 6;
    }else{
        diaFinalMesPassado = diaInicial-1;
    }
    diaFinal = diaInicial;
    for(aux = 1; aux < diasmeses[atual]; aux++){
        diaFinal = (diaFinal+1)%7;
    }
    gerarCalendario(diaInicial,atual,ano,$("#dias-calendario1"));
});

function construirDia(tag, diaSemana, dia, mes, ano){
    tag.attr('data-diaSemana', diaSemana);
    tag.attr('data-dia', dia);
    tag.attr('data-mes', mes);
    tag.attr('data-ano', ano);
    tag.click(function(){verificarHorarioDia(tag.attr('data-diaSemana'), tag.attr('data-dia'), tag.attr('data-mes'), tag.attr('data-ano'))})
}

function verificarHorarioDia(diaNaSemana, dia, mes, ano, modo){
    $('#dia-selecionado').html(diasabrev[diaNaSemana]+dia+"/"+mes);
    $('#dia-selecionado').attr('data-data',dia+"/"+mes+"/"+ano);

    //AJAX DE PROCURAR CONSULTAS DO DIA

    /* 
    //Construção de consulta

    IF COM O MODO PARA SABER SE ESTA NA PAGINA DE PERFIL OU PAINEL
    CASO NO PERFIL ELE FICARA NO MODAL DE REMARCAÇÃO E TEM DE HAVER UMA FUNÇÃO PARA HABILITAR O BOTÃO

    consulta = $(document.createElement('div'));
    consulta.addClass('consulta-disponivel');
    horario = $(document.createElement('span'));
    horario.addClass('horario-consulta');
    horario.html(horarioInicial+"-"+horarioFinal)
    icon = $(document.createElement('i'));
    icon.addClass('material-icons');
    icon.html('date_range');
    icon.attr('data-horaInicio',//);
    icon.attr('data-horaTermino',//);
    icon.attr('data-dia',//);
    icon.attr('data-mes',//);
    icon.attr('data-ano',//);


    icon.click(function(){modalAgendamento(icon.attr('data-horaInicio'),icon.attr('data-horaTermino'),icon.attr('data-dia'),
    icon.attr('data-mes'),icon.attr('data-ano'));})

    consulta.append(horario);
    consulta.append(icon);

    $('#consultas-disponiveis').append(consulta);
    */


}
