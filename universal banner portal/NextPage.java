import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class NextPage extends Template implements ActionListener
{

    JLabel label;
    JButton invest , loan;

    NextPage(String value)
    {

        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);

        label = new JLabel("Welcome:"+value);
        Dimension size = label.getPreferredSize();
        label.setBounds(40,50, size.width + 60, size.height);
        label.setFont(new Font("Century",Font.BOLD,17));
        label.setForeground (Color.blue);

        invest=new JButton("INVEST");
        Dimension bsize = invest.getPreferredSize();
        invest.setBounds(100,100, bsize.width, bsize.height);
        invest.addActionListener(this);

        loan=new JButton("LOAN");
        Dimension b2size = loan.getPreferredSize();
        loan.setBounds(300,100, b2size.width, b2size.height);
        loan.addActionListener(this);

        _header.add(label);
        _content.add(invest);
        _content.add(loan);

//        add(_content,BorderLayout.CENTER)
        ClockHome();
        this.setSize(500,450);
        this.setResizable(false);
        this.setVisible(true);
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
        if ( ae.getSource() == invest )
        {
            this.setVisible(false);
            Invest obj = new Invest();
        }

        if ( ae.getSource() == loan )
        {
            this.setVisible(false);
            Loan l = new Loan();
        }
    }

}
