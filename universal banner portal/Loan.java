import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Loan extends Template implements ActionListener {
    JButton SUBMIT ,PREVIOUS;
    JLabel label1,label2 , label3 , title ;
    final JTextField  text1,text2 , text3 ;

   public Loan()
    {

        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);

        title = new JLabel("Loan Portal");
        Dimension size = title.getPreferredSize();
        title.setBounds(40,50, size.width + 60, size.height);
        title.setFont(new Font("Century",Font.BOLD,17));
        title.setForeground (Color.blue);

        label1 = new JLabel();
        label1.setText("Amount :");
        label1.setForeground(Color.white);
        label1.setBounds(350,50, size.width, size.height);

        text1 = new JTextField(15);
        Dimension tsize = text1.getPreferredSize();
        text1.setBounds(500,50, tsize.width, tsize.height);
        text1.setToolTipText("Enter Amount of money you want ");

        label2 = new JLabel();
        label2.setText("Duration (Months) :");
        label2.setForeground(Color.white);
        label2.setBounds(350,100, size.width + 60, size.height);

        text2 = new JTextField(15);
        text2.setBounds(500,100, tsize.width, tsize.height);
        text2.setToolTipText("Enter Duration of Time ");

        SUBMIT=new JButton("SUBMIT");
        Dimension bsize = SUBMIT.getPreferredSize();
        SUBMIT.setBounds(350,200, bsize.width, bsize.height);
        SUBMIT.addActionListener(this);

        PREVIOUS = new JButton("PREVIOUS");
        Dimension b2size = PREVIOUS.getPreferredSize();
        PREVIOUS.setBounds(500, 200, b2size.width, b2size.height);
        PREVIOUS.addActionListener(this);

        label3 = new JLabel();
        label3.setText("Estimated EMI :");
        label3.setForeground(Color.white);
        label3.setBounds(350,150, size.width + 40, size.height);

        text3 = new JTextField(15);
        text3.setBounds(500,150, tsize.width, tsize.height);
        text3.setEditable( false );

        _header.add(title);
        _content.add(label1);
        _content.add(label2);
        _content.add(label3);
        _content.add(text1);
        _content.add(text2);
        _content.add(text3);
        _content.add(SUBMIT);
        _content.add(PREVIOUS);

        this.setSize(1000,400);
        this.setResizable(false);
        this.setVisible(true);
        text1.requestFocusInWindow();
    }

    public void actionPerformed(ActionEvent ae)
    {
        if ( ae.getSource() == exit )
        {
            this.setVisible(false);
            System.exit(0);
        }
        if ( ae.getSource() == minimize )
        {
            this.setState(this.ICONIFIED);
        }
        if ( ae.getSource() == SUBMIT )
        {
            text3.setText("1234");
        }
        if ( ae.getSource() == PREVIOUS )
        {
            this.setVisible(false);
            this.dispose();
            NextPage t = new NextPage("admin");
        }


    }
}
