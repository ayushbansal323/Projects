import javax.swing.*;
import java.awt.event.*;
import java.applet.*;
import java.awt.*;
import java.util.*;
import java.util.*;
import java.text.*;

abstract public class Temp extends JFrame
{
    public JPanel panel , panel2;
    JLabel header;
//	JButton back, forward;

    Temp()
    {
        this.setSize(950,600);
        this.setResizable(false);

        addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent w)
            {
                System.exit(0);
            }
        });

        setTitle("Universal Banking Portal");


        panel=new JPanel();
        panel.setBackground(new Color(255,255,255));
        panel.setLayout(null);

        header = new JLabel();
        header.setFont(new Font("Century",Font.BOLD,30));
        header.setText("Universal Banking Portal");
        header.setForeground (Color.blue);
        Dimension size = header.getPreferredSize();
        header.setBounds(300,90,size.width, size.height);

/*		back = new JButton("<-");
		Dimension bsize = back.getPreferredSize();
		back.setBounds(5,40,bsize.width, bsize.height);
		//back.setIcon(new ImageIcon("back.png"));

		forward = new JButton("->");
		forward.setBounds(6 + bsize.width,40,bsize.width, bsize.height);

		panel.add(back);
		panel.add(forward);
*/
        panel.add(header);

        Clock();
    }

    void Clock ()
    {
        ClockLabel dateLable = new ClockLabel("date");
        ClockLabel timeLable = new ClockLabel("time");
        ClockLabel dayLable = new ClockLabel("day");

        dateLable.setForeground (Color.blue);
        timeLable.setForeground (Color.blue);

        dateLable.setFont(new Font("Century",Font.BOLD,15));
        dateLable.setBounds(720,-5,200, 100);

        timeLable.setFont(new Font("Century",Font.BOLD,15));
        timeLable.setBounds(740,15,200, 100);

        panel.add(dateLable);
        panel.add(timeLable);
        panel.add(dayLable);


    }

/*	public void paint(Graphics g)
	{
		g.drawLine(100,300,321,500);
		g.drawImage(im,0,0,null);
	}
*/
}
