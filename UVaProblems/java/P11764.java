import java.io.*;
public class P11764 {
	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) throws Throwable{
		int cases = Integer.parseInt(in.readLine());
		for(int j=0; j < cases;j++){
			int len = Integer.parseInt(in.readLine());
			String [] walls = in.readLine().split(" ");
			int hi = 0;int low = 0;
			for (int i = 0; i < len-1 ; i++){
				if (Integer.parseInt(walls[i]) < Integer.parseInt(walls[i+1])){
					hi++;
				}
				else if (Integer.parseInt(walls[i]) > Integer.parseInt(walls[i+1])){
					low++;
				}
			}
			out.write("Case "+Integer.toString(j+1)+": "+Integer.toString(hi)+" "+Integer.toString(low)+"\n");
		}
		out.close();
	}
}
