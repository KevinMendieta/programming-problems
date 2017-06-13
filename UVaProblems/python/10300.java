import java.io.*;

public class Main{

	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws Throwable{
		int cases = Integer.parseInt(in.readLine());
		while (cases > 0){
			int numberFarmers = Integer.parseInt(in.readLine());
			long theSum = 0;
			for (int i = 0;i<numberFarmers;i++){
				String[] info = in.readLine().split(" ");
				long premiun = Long.parseLong(info[0])*Long.parseLong(info[2]);
				theSum += premiun;
			}
			out.write(Long.toString(theSum)+"\n");
			cases--;
		}
		out.close();
	}
}