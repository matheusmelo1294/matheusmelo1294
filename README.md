package temperatur;

import java.util.Scanner;

public class fisica {
	public static void main(String[] args) {
		System.out.println("OLÁ, DIGITE SEU NOME: ");
		Scanner entrada = new Scanner(System.in);
		System.out.println("DIGITE SEU NOME: ");
		String nome = entrada.next();
		System.out.println("SEJA BEM-VINDO");
		System.out.println(nome);
		System.out.println("IREI LHE AJUDAR A RESOLVER AS SEGUINTES EQUAÇÕES DE FÍSICA");
		
		System.out.println("COMEÇAREMOS COM A VELOCIDADE MÉDIA");
		System.out.println("DIGITE O ESPAÇO EM METROS: ");
		
		double espaco = entrada.nextDouble();
		System.out.println(espaco);
		
		System.out.println("DIGITE O TEMPO EM SEGUNDOS: ");
		
		double tempo = entrada.nextDouble();
		System.out.println(tempo);
		
		double velocidade = espaco/tempo;
		System.out.println("A VELOCIDADE É");
		System.out.println(velocidade);
		System.out.println("METROS POR SEGUNDO");
		
		System.out.println("AGORA IREMOS CALCULAR A ACELERAÇÃO. DIGITE A VELOCIDADE EM METROS POR SEGUNDO, POR GENTILEZA);");
		double vel = entrada.nextDouble();
		System.out.println(vel);
		
		System.out.println("DIGITE O TEMPO EM SEGUNDOS");
		
		double time = entrada.nextDouble();
		System.out.println(time);
		
		double aceleracao = vel/time;
		
		System.out.println("A ACELERAÇÃO É ");
		System.out.println(aceleracao);
		System.out.println("METROS POR SEGUNDO AO QUADRADO");
		
		System.out.println("AGORA VAMOS CALCULAR O TRABALHO DA FORÇA");
		System.out.println(nome);
		System.out.println("NÃO ESQUEÇA DE SEGUIR AS INSTRUÇÕES");
		
		System.out.println("DIGITE A FORÇA EM NEWTONS: ");
		
		double forca = entrada.nextDouble();
		
		System.out.println("DIGITE O DESLOCAMENTO EM METROS: ");
		
		double deslocamento = entrada.nextDouble();
		
		double trabalho = forca*deslocamento;
		System.out.println("O TRABALHO É");
		System.out.println(trabalho);
		System.out.println("JOULES");
		
		System.out.println(nome);
		System.out.println("JÁ OUVIU FALAR EM ENERGIA POTENCIAL GRAVITACIONAL?");
		System.out.println("IREMOS CALCULAR AGORA");
		System.out.println("DIGITE A MASSA EM kg");
		
		double massa = entrada.nextDouble();
		
		System.out.println("DIGITE A ALTURA EM METROS");
		
		double altura = entrada.nextDouble();
		
		double epg = massa*9.81*altura;
		System.out.println("A ENERGIA POTENCIAL GRAVITACIONAL É");
		System.out.println(epg);
		System.out.println("JOULES");
		
		System.out.println("ESTAMOS FINALIZANDO!!!!!");
		System.out.println("VAMOS CALCULAR A ENERGIA CINÉTICA");
		System.out.println("DIGITE A MASSA: ");
		
		double mass = entrada.nextDouble();
		
		System.out.println("DIGITE A VELOCIDADE");
		
		double velocity = entrada.nextDouble();
		
		double ec = (mass*velocity*velocity)/2;
		
		System.out.println("A ENERGIA CINÉTICA É");
		System.out.println(ec);
		System.out.println("JOULES\n\n\n");
		
		System.out.println(nome);
		System.out.println("MUITO OBRIGADO PELO DESEMPENHO, ESPERO TER AJUDADO");
		System.out.println("VOLTE SEMPRE!!!!");

		
	}

}
