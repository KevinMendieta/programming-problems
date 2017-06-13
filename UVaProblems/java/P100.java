import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class P100 {

	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	private static int[] numbers;

	public static int toInt(String a){
		return Integer.parseInt(a);
	}

	public static void preCalculate(int range){
		numbers = new int[range+1];
		numbers[0] = 0;
		for (int i = 1; i < numbers.length;i++){
			int cont = 1;
			int number = i;
			while(number!=1){
				if(number%2==0){
					number /= 2;
				}else{
					number = 3*(number)+1;
				}
				cont++;
			}
			numbers[i] = cont;
		}
		System.out.println("out");
	}
	public static int getMax(int i, int j){
		int max = numbers[i];
		for (int k = i ; k < j;k++){
			if(numbers[k]> max){
				max = numbers[k];
			}
		}
		return max;
	}
	public static void main(String[] args) throws Throwable{
		preCalculate(100000);
		String[] info = in.readLine().split(" ");
		while(info.length>1){
			out.write(info[0]+" "+info[1]+" "+getMax(toInt(info[0]),toInt(info[1]))+"\n");
			info = in.readLine().split(" ");
		}
		out.close();
	}
}
