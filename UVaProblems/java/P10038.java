import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;

public class P10038 {

	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws Throwable{
		HashSet<Integer> differences = null;
		HashSet<Integer> sequence = null;
		while (true){
			differences = new HashSet<Integer>();
			sequence = new HashSet<Integer>();
			String[] numbers = in.readLine().split(" ");
			if(Integer.parseInt(numbers[0])>1){
				for(int i = 1; i < Integer.parseInt(numbers[0]); i++){
					sequence.add(i);
				}
				for(int i = 1; i < Integer.parseInt(numbers[0]);i++){
					differences.add(Math.abs(Integer.parseInt(numbers[i])-Integer.parseInt(numbers[i+1])));
				}
				differences.retainAll(sequence);
				if(differences.equals(sequence)){
					out.write("Jolly\n");
				}else{
					out.write("Not jolly\n");
				}
			}else{
				out.write("Jolly\n");
			}
			break;
		}
		out.close();
	}
}
