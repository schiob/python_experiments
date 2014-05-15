import javax.swing.*;
import java.util.*;

public class Dado {
	public static void main(String[] args)
	{
		int numDado;
		Random random = new Random();
		numDado = random.nextInt(6) + 1;
		JOptionPane.showMessageDialog(null, "te salio: " + numDado);
		
	}
}
