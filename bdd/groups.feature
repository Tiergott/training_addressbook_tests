Feature: Group CRUD
  Description

  Scenario Outline: Add a new group
    Given a group list in Addressbook
    Given a new group with <name>, <header>, <footer>
    When  I add this group
    Then  a new group list is equal to old group list with this new group

    Examples:
    | name    | header | footer |
    | ADhbjh  | HJBSF  |  CGHC  |
    | Новая г | ПРМРПМ | Футер  |
    | ;%№%`' |        |        |


  Scenario: Delete a random group
    Given a non-empty group list in Addressbook
    Given a selected random group in this list
    When I delete this group
    Then a new list is equal to old list without this group
