#include <iostream>

using std::cout;
using std::endl;

enum Suit { CLUBS, SPADES, HEARTS, DIAMONDS };

class Card {
  public:
    Card(int r, Suit s);
    virtual int value();
    Suit suit();
  protected:
    int m_card;
  private:
    Suit m_suit;
};

Card::Card(int r, Suit s) :m_card(r), m_suit(s) {}

int Card::value() {
  return m_card;
}

Suit Card::suit() {
  return m_suit;
}

class BlackJackCard : public Card {
  public:
    BlackJackCard(int r, Suit s);
    int value();
  private:
/* deliberately empty */
};

BlackJackCard::BlackJackCard(int r, Suit s) : Card(r, s) {}

int BlackJackCard::value() {
  if (m_card == 1) {
    return 11;
  } else if (m_card < 10) {
    return m_card;
  } else {
    return 10;
  }
}

int main() {
  Card c(5, CLUBS);
  cout << "c is a " << c.value() << " of " << c.suit() << endl;
  BlackJackCard j(12, HEARTS);
  cout << "j is a " << j.value() << " of " << j.suit() << endl;
  BlackJackCard k(1, HEARTS);
  cout << "k is a " << k.value() << " of " << k.suit() << endl;
}
