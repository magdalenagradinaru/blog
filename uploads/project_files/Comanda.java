import javax.swing.*;
import java.awt.*;

public class Comanda extends JFrame {

    //Image IMG;

    JLabel myLabel;
    JLabel additionalLabel;
    TextField myText;
    JComboBox<String> pizzaDropDown;
    JCheckBox[] ingredientCheckBoxes;
    JCheckBox[] drinksCheckBoxes;
    Choice sideDishesChoice;
    JButton confirmButton;
    JRadioButton cashRadioButton;
    JRadioButton cardRadioButton;
    ButtonGroup paymentGroup;

    JTextField addressField;

    JTextField phoneNumberField;

    JTextArea commentsArea;

    JTextField discountCodeField;

    JLabel deliveryTimeLabel;

    int checkBoxYPosition = 280;



    public Comanda() {
        this.setLocation(100, 100);
        this.setSize(800, 700);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setResizable(true);
        this.setTitle("Comanda");
        this.getContentPane().setBackground(Color.PINK);

        this.setLayout(null);

        init();
    }



    public void paint(){
        //IMG=getIconImage("C:\\Users\\user\\IdeaProjects\\Glovo\\src");
    }



    // Metoda de inițializare
    public void init() {
        //JLabel principal
        myLabel = new JLabel("Bine ati venit pe pagina noastra!");
        myLabel.setForeground(new Color(55, 23, 218));
        myLabel.setFont(new Font("Arial", Font.BOLD, 16));
        myLabel.setBackground(Color.WHITE);
        myLabel.setBounds(50, 20, 680, 50);

        //  al doilea JLabel
        additionalLabel = new JLabel("Hai sa pregatim impreuna comanda ta.");
        additionalLabel.setForeground(new Color(255, 0, 0));
        additionalLabel.setFont(new Font("Arial", Font.PLAIN, 14));
        additionalLabel.setHorizontalAlignment(SwingConstants.CENTER);
        additionalLabel.setBackground(Color.LIGHT_GRAY);
        additionalLabel.setBounds(50, 80, 680, 30);

        //  TextField pentru nume
        myText = new TextField(" Introduceti numele dumneavoastra:");
        myText.setBounds(50, 160, 300, 30);


        // eticheta pentru categorii de pizza
        JLabel pizzaLabel = new JLabel("Alegeți tipul de pizza:");
        pizzaLabel.setBounds(50, 200, 200, 30);
        this.add(pizzaLabel);


        // JComboBox (drop-down) pentru denumiri de pizza
        String[] pizzaOptions = {"Margherita", "Pepperoni", "Quattro Stagioni", "Hawaiian", "Vegetarian"};
        pizzaDropDown = new JComboBox<>(pizzaOptions);
        pizzaDropDown.setBounds(50, 240, 300, 30);


        //  JCheckBox-uri pentru ingrediente adiționale
        String[] ingredients = {"Ciuperci", "Masline", "Becon", "Salam", "Cascaval"};
        ingredientCheckBoxes = new JCheckBox[ingredients.length];
        JLabel ingredientsLabel = new JLabel("Ingrediente adiționale:");
        ingredientsLabel.setBounds(50, 280, 200, 30);
        this.add(ingredientsLabel);

        for (int i = 0; i < ingredients.length; i++) {
            ingredientCheckBoxes[i] = new JCheckBox(ingredients[i]);
            ingredientCheckBoxes[i].setBounds(50, checkBoxYPosition+=40, 150, 30);
            this.add(ingredientCheckBoxes[i]);

        }


        // butonul de confirmare a comenzii
        confirmButton = new JButton("Confirmă comanda");
        confirmButton.setBounds(400, 530, 200, 30); // După Choice
        this.add(confirmButton);

        //butoane radio pentru achitare (cash/card)

        JLabel paymentLabel = new JLabel("Metodă de plată:");
        paymentLabel.setBounds(50, 520, 200, 30);
        this.add(paymentLabel);


        cashRadioButton = new JRadioButton("Cash");
        cashRadioButton.setBounds(50, 570, 100, 30);
        cardRadioButton = new JRadioButton("Card");
        cardRadioButton.setBounds(150, 570, 100, 30);

        paymentGroup = new ButtonGroup();
        paymentGroup.add(cashRadioButton);
        paymentGroup.add(cardRadioButton);

        // butoanele radio în fereastră
        this.add(cashRadioButton);
        this.add(cardRadioButton);

        // câmpuri pentru detalii de livrare
        JLabel addressLabel = new JLabel("Adresă de livrare:");
        addressLabel.setBounds(400, 120, 150, 30);
        addressField = new JTextField();
        addressField.setBounds(400, 160, 300, 30);

        JLabel phoneLabel = new JLabel("Număr de telefon:");
        phoneLabel.setBounds(400, 200, 150, 30);
        phoneNumberField = new JTextField();
        phoneNumberField.setBounds(400, 240, 300, 30);

        //textArea pentru comentarii
        JLabel commentsLabel = new JLabel("Comentarii:");
        commentsLabel.setBounds(400, 280, 150, 30);
        commentsArea = new JTextArea();
        commentsArea.setBounds(400, 320, 300, 60);
        commentsArea.setLineWrap(true);
        commentsArea.setWrapStyleWord(true);

        // câmp pentru cod reducere
        JLabel discountLabel = new JLabel("Cod reducere:");
        discountLabel.setBounds(400, 400, 150, 30);
        discountCodeField = new JTextField();
        discountCodeField.setBounds(400, 440, 150, 30);

        //  eticheta pentru estimare timp livrare
        deliveryTimeLabel = new JLabel("Estimare timp livrare: 30-45 minute");
        deliveryTimeLabel.setBounds(400, 480, 300, 30);

        // Adăugăm toate componentele în fereastră
        this.add(myLabel);
        this.add(additionalLabel);
        this.add(myText);
        this.add(pizzaDropDown);
        this.add(addressLabel);
        this.add(addressField);
        this.add(phoneLabel);
        this.add(phoneNumberField);
        this.add(commentsLabel);
        this.add(commentsArea);
        this.add(discountLabel);
        this.add(discountCodeField);
        this.add(deliveryTimeLabel);
    }

    public static void main(String[] args) {
        Comanda window = new Comanda();
        window.setVisible(true);
    }
}


