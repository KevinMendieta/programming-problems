import java.io.*;
import java.util.*;

public class P478 {
	public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in)) ;

	public static double area(double x1,double y1,double x2,double y2,double x3,double y3){
		double area = (x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0;
		return (area > 0) ? area : area*-1;
	}
	public static boolean inTriangle(double x1, double y1, double x2, double y2, double x3, double y3,double x,double y){
		double A = area(x1,y1,x2,y2,x3,y3);
		double A1 = area(x, y, x2, y2, x3, y3);
		double A2 = area(x1, y1, x, y, x3, y3);
		double A3 = area(x1, y1, x2, y2, x, y);
		return (A == A1+A2+A3);
	}

	public static boolean inCircle(double x1,double y1,double r ,double x, double y){
		return( ((x-x1)*(x-x1))+((y-y1)*(y-y1)) <= r*r);
	}

	public static boolean inRectangle(double x1,double y1,double x2,double y2,double x3,double y3){
		return(x1 <= x3 && x2 >= x3 && y1 <= y3 && y2 >= y3);
	}

	public static void main(String[] args)throws Throwable{
		String[] line = in.readLine().split(" ");
		ArrayList<String[]> map = new ArrayList<String[]>();
		ArrayList<String[]> points = new ArrayList<String[]>();
		while (line.length > 1){
			map.add(line);
			line = in.readLine().split(" ");
		}
		String[] poin = in.readLine().split(" ");
		while (!poin[0].equals("9999.9")){
			points.add(poin);
			poin = in.readLine().split(" ");
		}
		for (int i = 0; i < points.size();i++){
			boolean band = false;
			for (int j = 0; j < map.size();j++){
				if (map.get(j)[0].equals("t")){
					if(inTriangle(Double.parseDouble(map.get(j)[1]),Double.parseDouble(map.get(j)[2]),Double.parseDouble(map.get(j)[3]),Double.parseDouble(map.get(j)[4]),Double.parseDouble(map.get(j)[5]),Double.parseDouble(map.get(j)[6]),Double.parseDouble(points.get(i)[0]),Double.parseDouble(points.get(i)[1]))){
						out.write("Point "+Integer.toString(i+1)+" is cointained in figure "+Integer.toString(j+1)+"\n");
						band = true;
					}
				}else if(map.get(j)[0].equals("r")){
					if(inRectangle(Double.parseDouble(map.get(j)[1]),Double.parseDouble(map.get(j)[2]),Double.parseDouble(map.get(j)[3]),Double.parseDouble(map.get(j)[4]),Double.parseDouble(points.get(i)[0]),Double.parseDouble(points.get(i)[1]))){
						out.write("Point "+Integer.toString(i+1)+" is cointained in figure "+Integer.toString(j+1)+"\n");
						band = true;
					}
				}else if(map.get(j)[0].equals("c")){
					if(inCircle(Double.parseDouble(map.get(j)[1]),Double.parseDouble(map.get(j)[2]),Double.parseDouble(map.get(j)[3]),Double.parseDouble(points.get(i)[0]),Double.parseDouble(points.get(i)[1]))){
						out.write("Point "+Integer.toString(i+1)+" is cointained in figure "+Integer.toString(j+1)+"\n");
						band = true;
					}
				}
			}
			if (!band){
				out.write("Point "+Integer.toString(i+1)+" is not cointained in any figure"+"\n");
			}
		}
		out.close();
	}
}
