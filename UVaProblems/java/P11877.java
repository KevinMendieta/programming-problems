import java.io.*;

public class P11877 {
	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args)throws Throwable{
		int bottle = Integer.parseInt(in.readLine());
		while (bottle > 0){
			out.write(Integer.toString(bottle/2)+"\n");
			bottle = Integer.parseInt(in.readLine());
		}
		out.close();
	}
}
