import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;;

public class P119 {

	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws Throwable{
		int size;
		HashMap<String,Integer> friendsValues = new HashMap<String,Integer>();
		while (in.ready()){
			size = Integer.parseInt(in.readLine());
			String[] friends = in.readLine().split(" ");
			for(int i = 0 ; i < friends.length ; i++){
				friendsValues.put(friends[i], 0);
			}
			String[] info = null;
			for(int i = 0; i < size; i++){
				info = in.readLine().split(" ");
				if(Integer.parseInt(info[2])!=0 && Integer.parseInt(info[1])%Integer.parseInt(info[2])!=0)info[1] = (Integer.parseInt(info[1]) - (Integer.parseInt(info[1])%Integer.parseInt(info[2])))+"";
				if(Integer.parseInt(info[2])!=0)friendsValues.put(info[0],-Integer.parseInt(info[1])+friendsValues.get(info[0]));
				for (int j = 3; j < Integer.parseInt(info[2])+3;j++){
					if(Integer.parseInt(info[2])!=0)friendsValues.put(info[j],friendsValues.get(info[j])+(Integer.parseInt(info[1])/Integer.parseInt(info[2])));
				}
			}
			for(int i = 0; i<friends.length; i++){
				out.write(friends[i]+" "+friendsValues.get(friends[i])+"\n");
			}
			if(in.ready())out.write("\n");
		}
		out.close();
	}
}
