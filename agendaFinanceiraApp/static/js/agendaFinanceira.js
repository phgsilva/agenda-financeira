
$(document).ready(function () {
    $("#id_data_vencimento").datepicker({ dateFormat: "dd/mm/yy" });
    $("#id_data_entrada").datepicker({ dateFormat: "dd/mm/yy" });
    $("#txbDataInicio").datepicker({ dateFormat: "dd/mm/yy" });
    $("#txbDataFim").datepicker({ dateFormat: "dd/mm/yy" });
});

function validarValor() {
    var valor = parseInt($("#id_valor").value);

    if(isNaN(valor)){
        alert('O conteúdo para o campo "Valor" deve ser um numero!');
        return false;
    }
}

