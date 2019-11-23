%------------------fact-------------------
male(phillip).
male(charles).
male(harry_duke).
male(william).
male(george).
male(louis).
male(harrison).
male(timothy_laurence).
male(mark_phillips).
male(peter_phillips).
male(mike).
male(andrew).
male(edward).
male(james).


female(elizabeth).
female(camilla).
female(diana).
female(kate).
female(charlotte).
female(meghan).
female(anne).
female(autumn).
female(zara).
female(sophie).
female(louise_windsor).
female(sarah).
female(beatrice).
female(eugeine).

married(elizabeth, phillip).
married(phillip, elizabeth).
married(charles, camilla).
married(camilla, charles).
married(william, kate).
married(kate, william).
married(harry_duke, meghan).
married(meghan, harry_duke).
married(anne, timothy_laurence).
married(timothy_laurence, anne).
married(peter_phillips, autumn).
married(autumn, peter_phillips).
married(zara, mike).
married(mike, zara).
married(sarah, andrew).
married(andrew, sarah).
married(edward, sophie).
married(sophie, edward).

divorced(diana, charles).
divorced(charles, diana).
divorced(mark_phillips, anne).
divorced(anne, mark_phillips).

% the he 1
parent(elizabeth, charles).
parent(elizabeth, anne).
parent(elizabeth, andrew).
parent(elizabeth, edward).
parent(phillip, charles).
parent(phillip, anne).
parent(phillip, andrew).
parent(phillip, edward).

% the he 2
parent(charles, william).
parent(charles, harry_duke).
parent(diana, william).
parent(diana, harry_duke).

parent(mark_phillips, peter_phillips).
parent(mark_phillips, zara).
parent(anne, peter_phillips).
parent(anne, zara).

parent(sarah, beatrice).
parent(sarah, eugeine).
parent(andrew, beatrice).
parent(andrew, eugeine).

parent(sophie, james).
parent(sophie, louise_windsor).
parent(edward, james).
parent(edward, louise_windsor).

% the he 3
parent(william, george).
parent(william, charlotte).
parent(william, louis).
parent(kate, george).
parent(kate, charlotte).
parent(kate, louis).

parent(harry_duke, harrison).
parent(meghan, harrison).

% -----------------rules---------------------
% chong
husband(Person, Wife) :-
	married(Person, Wife),
	male(Person).

% vo
wife(Person, Husband) :-
	married(Person, Husband),
	female(Person).

% bo
father(Parent, Child) :-
	parent(Parent, Child),
	male(Parent).

% me
mother(Parent, Child) :-
	parent(Parent, Child),
	female(Parent).

% con cai
child(Child, Parent) :-
	parent(Parent, Child).

% con trai
son(Child, Parent) :-
	child(Child, Parent),
	male(Child).

% con gai
daughter(Child, Parent) :-
	child(Child, Parent),
	female(Child).

% ong ba
grandparent(GrandParent, GrandChild) :-
	parent(GrandParent, Parent),
	parent(Parent, GrandChild).

% ba
grandmother(GrandMother, GrandChild) :-
	female(GrandMother),
    grandparent(GrandMother, GrandChild).

% ong
grandfather(GrandFather, GrandChild) :-
    male(GrandFather),
	grandparent(GrandFather, GrandChild).

% chau
grandchild(GrandChild, GrandParent):-
    grandparent(GrandParent, GrandChild).

% chau trai
grandson(GrandSon, GrandParent) :-
	grandparent(GrandParent, GrandSon),
    male(GrandSon).

% chau gai
granddaughter(GrandDaughter, GrandParent) :-
	grandparent(GrandParent, GrandDaughter),
    female(GrandDaughter).

% A sibling is having one or both parents in common
% anh em ruoi co 1 hoac ca bo va me
sibling(Person1, Person2):-
    father(Father, Person1),
    father(Father, Person2),
    mother(Mother, Person1),
    mother(Mother, Person2),
	Person1 \= Person2.

% con trai ruot
brother(Person, Sibling) :-
	sibling(Person, Sibling),
	male(Person).

% con gai ruot
sister(Person, Sibling) :-
	sibling(Person, Sibling),
	female(Person).

% An aunt is a person who is the sister of a parent,
% or the wife of one s uncle

% di la con gai cua bo me hoac la vo cua chu
aunt(Person, NieceNephew) :-  % di cua chau trai, chau gai
	sister(Person, Parent), % di la chi,em gai voi bo me
	parent(Parent, NieceNephew).

aunt(Person, NieceNephew) :-
	wife(Person, Uncle), % di ket hon voi chu
	brother(Uncle, Parent), % chu la anh,em trai voi bo me
	parent(Parent, NieceNephew).

% chu
uncle(Person, NieceNephew) :-
	brother(Person, Parent),
	parent(Parent, NieceNephew).

uncle(Person, NieceNephew) :-
	husband(Person, Aunt),
	sister(Aunt, Parent),
	parent(Parent, NieceNephew).

% chau gai
niece(Person, AuntUncle) :-
	uncle(AuntUncle, Person),
	female(Person).

niece(Person, AuntUncle) :-
	aunt(AuntUncle, Person),
	female(Person).

% chau trai
nephew(Person, AuntUncle) :-
	uncle(AuntUncle, Person),
	male(Person).

nephew(Person, AuntUncle) :-
	aunt(AuntUncle, Person),
	male(Person).


