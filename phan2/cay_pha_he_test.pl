1. Liệt kê những người có giới tính là nam?
male(X).

2. Harry có có phải là con của Charles không?
child(harry_duke, charles).

3. Cha của George là ai?
father(X, george).

4. Diana và Charles có phải là vợ chồng không?
married(diana, charles).

5. Chồng của Anne là ai?
husband(X, anne).

6. Liệt kê các con trai của Elizabeth?
findall(X, son(X, elizabeth), Son).

7. Con của William là ai?
findall(X, child(X, william), Children).

8. Các con gái của Sarah?
findall(X, daughter(X, sarah), Daughter).

9. Ai là ông của James?
grandfather(X, james).

10. Anh em ruột của Andrew?
findall(X, sibling(andrew, X), Siblings).

11. Meghan là dì của ai?
findall(X, aunt(meghan, X), NieceNephew).

12. Anh trai của Zara Phillips là ai?
findall(X, brother(X, zara), Brother).

13.Tìm tất cả cháu (quan hệ ông/bà cháu) của nữ hoàng?
grandchild(X, 'elizabeth').

14. Anne và Harry Duke có phải quan hệ dì cháu không?
aunt(anne, harry_duke).
15. Ai vừa là cậu của William và Peter Phillip?
uncle(X, william), uncle(X, peter_phillips).

16. Cháu gái của Phillip ma còn độc thân?
findall(X, (granddaughter(X, phillip), not(married(X, Y))), FA_granddaughter).

17. Harrison và George có cùng ông hay không?
grandfather(X, harrison), grandfather(X, george).

18. Cháu trai của Harry_Duke là ai?
nephew(X,harry_duke).

19. Ai là chị/em gái của George?
findall(X, sister(X, 'george'), Sister).

20. James có phải là con của Anne?
child(james, Anne).