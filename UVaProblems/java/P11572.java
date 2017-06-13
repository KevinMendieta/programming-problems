import java.io.*;
import java.util.*;
public class P11572{
	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) throws Throwable{
		int cases = Integer.parseInt(in.readLine());
		int len;
		while(cases > 0){
			len = Integer.parseInt(in.readLine());
			int index = 0;int maxi = 0; int max = 0;
			ArrayList<Integer> flakes = new ArrayList<Integer>();
			HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
			for(int i = 0 ; i < len ; i++){
				flakes.add(Integer.parseInt(in.readLine()));
			}
			while(index < len){
				if (!map.containsKey(flakes.get(index))){
					map.put(flakes.get(index),index);
					max++;
					index++;
					}
				else{
					max = 0;
					index = map.get(flakes.get(index))+1;
					map.clear();
				}
				if(max > maxi){
					maxi = max;
				}
			}
			out.write(Integer.toString(maxi)+"\n");
			cases--;
		}
		out.close();
	}
}
