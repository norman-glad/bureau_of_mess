package exercise2;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.SwingUtilities;
import javax.swing.SwingWorker;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.awt.event.ActionEvent;

public class fibonacci extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField textNum;
	private JTextArea textArea = new JTextArea();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> new fibonacci().setVisible(true));
	}

	/**
	 * Create the frame.
	 */
	public fibonacci() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 498, 329);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);

		textNum = new JTextField();
		textNum.setColumns(10);

		JButton btnGenerate = new JButton("generate");
		btnGenerate.addActionListener(e -> fibGenerator());

		JLabel lblNewLabel = new JLabel("Number of terms ");

		GroupLayout gl_contentPane = new GroupLayout(contentPane);
		gl_contentPane.setHorizontalGroup(gl_contentPane.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_contentPane.createSequentialGroup().addGap(49)
						.addGroup(gl_contentPane.createParallelGroup(Alignment.LEADING)
								.addComponent(textArea, GroupLayout.PREFERRED_SIZE, 435, GroupLayout.PREFERRED_SIZE)
								.addGroup(gl_contentPane.createSequentialGroup().addComponent(lblNewLabel).addGap(18)
										.addComponent(textNum, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
												GroupLayout.PREFERRED_SIZE)
										.addGap(87).addComponent(btnGenerate)))
						.addContainerGap(34, Short.MAX_VALUE)));
		gl_contentPane.setVerticalGroup(gl_contentPane.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_contentPane.createSequentialGroup().addGap(20)
						.addGroup(gl_contentPane.createParallelGroup(Alignment.BASELINE).addComponent(lblNewLabel)
								.addComponent(textNum, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
										GroupLayout.PREFERRED_SIZE)
								.addComponent(btnGenerate))
						.addGap(18).addComponent(textArea, GroupLayout.PREFERRED_SIZE, 199, GroupLayout.PREFERRED_SIZE)
						.addContainerGap(20, Short.MAX_VALUE)));
		contentPane.setLayout(gl_contentPane);
	}

	private void fibGenerator() {
		// TODO Auto-generated method stub
		int count;
		try {
			count = Integer.parseInt(textNum.getText());
		} catch (NumberFormatException ex) {
			JOptionPane.showMessageDialog(this, "Invalid input");
			return;
		}

		textArea.setText("");
		new FibonacciWorker(count).execute();
	}

	private class FibonacciWorker extends SwingWorker<List<Integer>, Integer> {
		private final int count;

		public FibonacciWorker(int count) {
			this.count = count;
		}

		@Override
		protected List<Integer> doInBackground() throws Exception {
			// TODO Auto-generated method stub
			List<Integer> fibSeries = new ArrayList<>();
			int a = 0, b = 1;
			fibSeries.add(a);
			publish(a);
			Thread.sleep(2000);


			for (int i = 0; i < count; i++) {
				fibSeries.add(b);
				publish(b);
				int temp = a + b;
				a = b;
				b = temp;

				Thread.sleep(2000);
			}

			return fibSeries;
		}

		@Override
		protected void process(List<Integer> chunks) {
			for (Integer num : chunks) {
				textArea.append(num + "\n");
			}
		}

		@Override
		protected void done() {
			try {
				List<Integer> result = get();

				// Reverse order console print using Lambda
				System.out.println("\nReverse Order Fibonacci Series:");
				Collections.reverse(result);
				result.forEach(System.out::println);

			} catch (InterruptedException | ExecutionException e) {
				e.printStackTrace();
			}
		}
	}
}
