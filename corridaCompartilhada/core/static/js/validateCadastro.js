var form = document.getElementById("form-cadastro");

document.getElementById("btn-cadastrar").addEventListener("click", function () {
    if(document.getElementById("cpf").classList.contains('is-invalid')){
        document.getElementById("cpf").value = ''
    }else if(document.getElementById("dataNascimento").classList.contains('is-invalid')){
        document.getElementById("dataNascimento").value = ''
    }else{
        form.action = "{{corrida.cadastro}}"
        form.submit();
    }
});


function validaCPF(cpf)
  {
    document.getElementById("cpf").classList.remove('is-invalid');
    document.getElementById("cpf").classList.remove('is-valid');
    var numeros, digitos, soma, i, resultado, digitos_iguais;
    digitos_iguais = 1;
    if (cpf.length < 11)
         document.getElementById("cpf").classList.add('is-invalid');
    for (i = 0; i < cpf.length - 1; i++)
          if (cpf.charAt(i) != cpf.charAt(i + 1))
                {
                digitos_iguais = 0;
                break;
                }
    if (!digitos_iguais)
          {
          numeros = cpf.substring(0,9);
          digitos = cpf.substring(9);
          soma = 0;
          for (i = 10; i > 1; i--)
                soma += numeros.charAt(10 - i) * i;
          resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
          if (resultado != digitos.charAt(0))
                document.getElementById("cpf").classList.add('is-invalid');
          numeros = cpf.substring(0,10);
          soma = 0;
          for (i = 11; i > 1; i--)
                soma += numeros.charAt(11 - i) * i;
          resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
          if (resultado != digitos.charAt(1))
                document.getElementById("cpf").classList.add('is-invalid');
          document.getElementById("cpf").classList.add('is-valid');
          }
    else
        document.getElementById("cpf").classList.add('is-invalid');
  }

  function maiorDeIdade(dataNascimento) {
    document.getElementById("dataNascimento").classList.remove('is-invalid');
    document.getElementById("dataNascimento").classList.remove('is-valid');
    var userDob = new Date(dataNascimento);
    var maxDob = new Date();

    maxDob.setFullYear(maxDob.getFullYear() - 18);
    if (userDob <= maxDob){
         document.getElementById("dataNascimento").classList.add('is-valid');
    }else{
         document.getElementById("dataNascimento").classList.add('is-invalid');
    }
}