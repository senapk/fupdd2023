

//entrada 0 ou 1
//saida: "empate", "jog1", "jog2", "jog3"
function zerim(jog1, jog2, jog3) {
    
    let resultado = "";

    if (jog1 == jog2 && jog1 == jog3) {
        resultado = "empate";
    } else if (jog2 == jog3) {
        resultado = "jog1";
    } else if (jog1 == jog3) {
        resultado = "jog2";
    } else {}
        resultado = "jog3";
    
        return resultado;

}

