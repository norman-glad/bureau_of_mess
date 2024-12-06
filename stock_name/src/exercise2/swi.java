package exercise2;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ExecutionException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.SwingWorker;




public class swi extends JFrame {
    private JTextField numberField;
    private JButton generateButton;
    private JTextArea resultArea;

    public swi() {
        setTitle("Fibonacci Series Generator");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel inputPanel = new JPanel();
        numberField = new JTextField(10);
        generateButton = new JButton("Generate");
        inputPanel.add(new JLabel("Number of Fibonacci Series:"));
        inputPanel.add(numberField);
        inputPanel.add(generateButton);

        resultArea = new JTextArea();
        resultArea.setEditable(false);

        add(inputPanel, BorderLayout.NORTH);
        add(new JScrollPane(resultArea), BorderLayout.CENTER);

        generateButton.addActionListener(e -> generateFibonacciSeries());
    }

    private void generateFibonacciSeries() {
        int count;
        try {
            count = Integer.parseInt(numberField.getText());
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Invalid input");
            return;
        }

        resultArea.setText("");
        new FibonacciWorker(count).execute();
    }

    private class FibonacciWorker extends SwingWorker<List<Integer>, Integer> {
        private final int count;

        public FibonacciWorker(int count) {
            this.count = count;
        }

        @Override
        protected List<Integer> doInBackground() throws Exception {
            List<Integer> fibSeries = new ArrayList<>();
            int a = 0, b = 1;
            
            for (int i = 0; i < count; i++) {
                fibSeries.add(b);
                int temp = a + b;
                a = b;
                b = temp;
                publish(b);
                Thread.sleep(2000);
            }
            
            return fibSeries;
        }

        @Override
        protected void process(List<Integer> chunks) {
            for (Integer num : chunks) {
                resultArea.append(num + "\n");
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

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new swi().setVisible(true);
        });
    }
}