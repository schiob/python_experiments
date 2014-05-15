import java.util.Arrays;

public class arreglo{
	public static void main(String []args){
		int [][] p = {{1, 2, 3, 4}, {3, 4 ,5 ,6 ,3}, {3, 3, 4}};
		
		for (int []x : p){
			for (int y : x){
				System.out.println(y);
			}
		}
		
		Arrays.sort(p[0]);

		for (int []x : p){
			for (int y : x){
				System.out.println(y);
			}
		}
		
	}
}