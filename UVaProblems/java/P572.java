import java.io.*;
import java.util.*;
public class P572 {

	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

	public static ArrayList<ArrayList<String>> fillDown(ArrayList<ArrayList<String>> mat,int[] inds){
		 ArrayList<int[]> stack= new ArrayList<int[]>();
		 stack.add(inds);
		return mat;
	}
	public static String solve(ArrayList<ArrayList<String>> mat){
		int cont = 0;
		for(int i = 0; i < mat.size();i++){
			for (int j = 0; j < mat.get(0).size();j++){
				if(mat.get(i).get(j) == "@"){
					int i1 = i;int j1=j;
					cont++;
					int [] inds = [i1,j1];
					mat = fillDown(mat,inds);
				}
			}
		}
		return(Integer.toString(cont));
	}
	public static void main(String[] args)throws Throwable{
		String[] info = br.readLine().split(" ");
		while (!(Integer.parseInt(info[0]) == 0)){
			ArrayList<ArrayList<String>> mat = new ArrayList<ArrayList<String>>();
			System.out.println(Integer.parseInt(info[0]));
			for(int i = 0; i < Integer.parseInt(info[0]); i++){
				String[] line =br.readLine().split("");
				ArrayList<String> line2 = new ArrayList<String>();
				for(int j = 0; j<line.length;j++){
					line2.add(line[j]);
				}
				mat.add(line2);
			}
			out.write(solve(mat));
		}
		out.close();
	}
}
