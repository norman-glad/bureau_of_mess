package exercise1;

public class Account {
	private double bal; 
	public Account (double balance) {
		this.bal= balance; 
	}
	public synchronized void deposit(double amt) {
		if (amt>0) {
			bal+= amt; 
			System.out.println("deposit amt $"+amt);
			System.out.println("updated bal $"+bal);
			
		}
	}
	public synchronized void withdraw(double amt) {
		if (amt>0 && bal>=amt) {
			bal -= amt; 
		} else {
			System.out.println("insufficient bal $"+bal);
			}
	}
	public synchronized double getBal() {return bal;}
}
