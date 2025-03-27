public class Principal {
    public static void main(String[] args) {
        // Declaração de uma varíavel do tipo Contador
        Contador contador;

        // Criação de uma instância da classe Contador: um objeto
        contador = new Contador();
        // Se a propriedade registro fosse publica, poderia ser acessada diretamente
        // contador.registro = 10;
        // Como não é, devemos usar o método setRegistro
        contador.setRegistro(10);
        // Da mesma forma, para acessar o valor de registro, devemos usar o método getRegistro
        System.out.print(contador.getRegistro());
    }
}
