import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class P11151 {

	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void memo(String string)throws Throwable{
		int[][] mat = new int[string.length()][string.length()];
		for (int i = 0; i < string.length();i++){
			mat[i][i] = 1;
		}
		for (int cl=2; cl<=string.length(); cl++){
            for (int i=0; i<string.length()-cl+1; i++){
                int j = i+cl-1;
                if (string.charAt(i) == string.charAt(j) && cl == 2)
                   mat[i][j] = 2;
                else if (string.charAt(i) == string.charAt(j))
                   mat[i][j] = mat[i+1][j-1] + 2;
                else
                   mat[i][j] = Math.max(mat[i][j-1], mat[i+1][j]);
            }
        }
		for (int i = 0; i<string.length();i++){
			for (int j = 0; j<string.length();j++){
				out.write(mat[i][j]+" ");
			}
			out.write("\n");
		}
	}

	public static void main(String[] args) throws Throwable{
		int cases = Integer.parseInt(in.readLine());
		while(cases > 0){
			String string = in.readLine();
			memo(string);
			cases--;
		}
		out.close();
	}
}
