/**
 * Created by H4 on 14/08/2016.
 */
var App = App || {};

App.FormularioController = {
    listen: function () {
        var date = new Date();
        $(".datepicker").datepicker({
            changeMonth: true,
            changeYear: true,
            yearRange: 'c-130:c'
        });
        $('#cep').keyup(function () {
            App.FormularioController.buscaCep(this.value);
        });
        $('#formulario1').submit(function (event) {
           if(!App.FormularioController.validaCPF($('#cpf').val())){
               alert("CPF Inválido! Informe o CPF corretamente!");
               $('#cpf').val('');
               $('#cpf').focus();
               return false
           }
           return true;
        });
    },
    buscaCep: function (cep) {
        cep = cep.replace(/[^0-9]/g, '');
        if (cep.length != 8) {
            return false;
        }
        var url = 'https://viacep.com.br/ws/' + cep + '/json/';
        App.FormularioController.limparEndereco();
        $.getJSON(url, {}, function (result) {
            if (result.erro == true) {
                alert("Erro ao buscar CEP! Verifique o CEP informado!");
                $('[name^=cep]').removeAttr('disabled');
                return false;
            }
            $('#rua').val(result.logradouro);
            $('#bairro').val(result.bairro);
            $('#complemento').val(result.complemento);
            $('#cidade').val(result.localidade);
            $('#estado').val(result.uf);
            $('.endereco').removeAttr('disabled');
            $('#numero').focus();
        })
    },
    limparEndereco: function () {
        $('#rua').val('');
        $('#numero').val('');
        $('#bairro').val('');
        $('#complemento').val('');
        $('#cidade').val('');
        $('#estado').val('');
        $('.endereco').attr('disabled');
    },
    sleep: function (milliseconds) {
        var start = new Date().getTime();
        for (var i = 0; i < 1e7; i++) {
            if ((new Date().getTime() - start) > milliseconds) {
                break;
            }
        }
    },
    validaCPF: function (strCPF) {
        strCPF = strCPF.replace(/[^0-9]/g,''); // Remove o que não for numero.
        var Soma;
        var Resto;
        Soma = 0;

        // Elimina CPFs invalidos conhecidos
        if (strCPF.length != 11 || strCPF == "00000000000" || strCPF == "11111111111" || strCPF == "22222222222" ||
            strCPF == "33333333333" || strCPF == "44444444444" || strCPF == "55555555555" || strCPF == "66666666666" ||
            strCPF == "77777777777" || strCPF == "88888888888" || strCPF == "99999999999"
        ){
            return false;
        }

        for (i=1; i<=9; i++){
            Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
        }
        Resto = (Soma * 10) % 11;

        if ((Resto == 10) || (Resto == 11)){
            Resto = 0;
        }
        if (Resto != parseInt(strCPF.substring(9, 10)) ){
            return false;
        }

        Soma = 0;
        for (i = 1; i <= 10; i++){
            Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i)
        }
        Resto = (Soma * 10) % 11;

        if ((Resto == 10) || (Resto == 11)){
            Resto = 0
        }
        return Resto == parseInt(strCPF.substring(10, 11));
    },
};