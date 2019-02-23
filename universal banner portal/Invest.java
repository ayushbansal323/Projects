import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Invest extends Template implements ActionListener {

    JButton SUBMIT , PREVIOUS ;
    JLabel label1,label2 , label3 , title , choice;
    final JTextField  text1,text2 , text3 ;
    JComboBox <String>list;
	JCheckBox kyc;

    public Invest() {
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);

        title = new JLabel("Investment Portal");
        Dimension size = title.getPreferredSize();
        title.setBounds(40, 50, size.width + 80, size.height);
        title.setFont(new Font("Century", Font.BOLD, 17));
        title.setForeground(Color.blue);

        label1 = new JLabel();
        label1.setText("Amount :");
        label1.setForeground(Color.white);
        label1.setBounds(350, 50, size.width, size.height);

        text1 = new JTextField(15);
        Dimension tsize = text1.getPreferredSize();
        text1.setBounds(500, 50, tsize.width, tsize.height);
        text1.setToolTipText("Enter Amount of money you want ");

        label2 = new JLabel();
        label2.setText("Duration (Months) :");
        label2.setForeground(Color.white);
        label2.setBounds(350, 100, size.width + 60, size.height);

        text2 = new JTextField(15);
        text2.setBounds(500, 100, tsize.width, tsize.height);
        text2.setToolTipText("Enter Duration of Time ");

        SUBMIT = new JButton("CALCULATE");
        Dimension bsize = SUBMIT.getPreferredSize();
        SUBMIT.setBounds(350, 300, bsize.width, bsize.height);
        SUBMIT.addActionListener(this);

        PREVIOUS = new JButton("PREVIOUS");
        Dimension b2size = PREVIOUS.getPreferredSize();
        PREVIOUS.setBounds(500, 300, b2size.width, b2size.height);
        PREVIOUS.addActionListener(this);

        label3 = new JLabel();
        label3.setForeground(Color.white);
        label3.setText("Estimated Amount :");
        label3.setBounds(350, 200, size.width + 40, size.height);

        text3 = new JTextField(15);
        text3.setBounds(500, 200, tsize.width, tsize.height);
        text3.setEditable(false);

        choice = new JLabel();
        choice.setForeground(Color.white);
        choice.setText("Investment Method :");
        choice.setBounds(350, 150, size.width + 50, size.height + 10);

        list = new JComboBox<String>();
        Dimension lsize = list.getPreferredSize();
        list.setBounds(500, 150, lsize.width + 100, lsize.height);
        list.addItem("S.I.P");
        list.addItem("Fixed Deposite");

		UIManager.put("CheckBox.disabledText", UIManager.get("CheckBox.foreground"));
		kyc = new JCheckBox("KYC");
        kyc.setForeground(Color.white);
        kyc.setBackground(new Color(0,70,150));
		Dimension csize = kyc.getPreferredSize();
		kyc.setBounds(350 , 250 ,csize.width , csize.height );

		kyc.addActionListener(this);

        _header.add(title);
        _content.add(label1);
        _content.add(label2);
        _content.add(label3);
        _content.add(text1);
        _content.add(text2);
        _content.add(text3);
        _content.add(SUBMIT);
        _content.add(choice);
        _content.add(list);
        _content.add(PREVIOUS);

	_content.add(kyc);


        this.setSize(1000,500);
        this.setResizable(false);
        this.setVisible(true);
        text1.requestFocusInWindow();
    }

    public void actionPerformed(ActionEvent ae) {

        if ( ae.getSource() == exit )
        {
            this.setVisible(false);
            System.exit(0);
        }
        if ( ae.getSource() == minimize )
        {
            this.setState(this.ICONIFIED);
        }

        if ( ae.getSource() == PREVIOUS )
        {
            this.setVisible(false);
            this.dispose();
            NextPage t = new NextPage("admin");
        }

        if (ae.getSource() == SUBMIT) {
			if(kyc.isSelected())
            {
                if ((list.getItemAt(list.getSelectedIndex())).equals("S.I.P")) {
                    text3.setText("S.I.P");
                    text3.setToolTipText("Estimated amount if invested in Systematic Investement Plan ");
                }

                if ((list.getItemAt(list.getSelectedIndex())).equals("Fixed Deposite")) {
                    text3.setText("FIXED");
                    text3.setToolTipText("Estimated amount if invested in Fixed Deposite Plan ");
                }
            }
        }
    }
}

class demo
{
	public static void main(String arg[])
	{
		try
		{
			Invest frame=new Invest();
		}
		catch(Exception e)
		{JOptionPane.showMessageDialog(null, e.getMessage());}
}
}