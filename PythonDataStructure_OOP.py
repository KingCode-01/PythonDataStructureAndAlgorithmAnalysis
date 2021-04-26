'''
    Python OOP(面向对象)
    定义函数:
        之前的过程抽象例子调用了Python数学模块中的sqrt函数来计算平方根.
        通常来说,可以通过定义函数来隐藏任何计算的细节.
        函数的定义需要一个函数名,一系列参数以及一个函数体.
        函数也可以显式地返回一个值.

        例如:
            定义简单的函数会返回传入值的平方根.

            def square(n):
                return n ** 2

            s = square(3)
            print(s)

        这个函数定义包含函数名square以及一个括号包含的形式参数列表.
        在这个函数中,n是唯一的形式参数,这意味着square只需要一份数据就能完成任务.
        计算n ** 2 并返回结果的细节,被隐藏起来.
        如果要调用square函数,可以为其提供一个实际参数值,并要求Python环境计算.
        * square函数的返回值可以作为参数传递给另一个函数调用.


    运用著名的牛顿迭代法,可以自己实现平方根函数:

    newguess = 1/2*(oldguess + n/oldguess)

    以上公式接受一个值n,通过在每一次迭代中将newguess赋值给oldguess来反复猜测平方根.
    初次猜测的平方根是n/2.

    以下函数展示了该函数的定义,它接受值n并且返回20轮迭代之后的n的平方根,
    牛顿迭代法的细节都被隐藏在函数定义之中,用户不需要知道任何实现细节就可以调用该函数来求平方根.

        def squareroot(n):
            root = n / 2
            for k in range(20):
                root = (1 / 2) * (root + (n / root))
            return root

        if __name__ == '__main__':

            s = squareroot(9)
            print(s)

        # 3.0

    Python定义类:
        使用了抽象数据类型来对数据对象的状态及行为进行逻辑描述,通过构建能实现抽象数据类的类,
        可以利用抽象过程,同时为真正在程序中运用抽象提供必要的细节.每当需要实现抽象数据类型时,就可以创建新类.
        Fraction类:
            要展示如何实现用户定义的类,一个常用的例子是构建实现抽象数据类型Fraction的类.
            Python提供了很多数值类,但是在有些时候,需要创建"看上去很像"分数的数据对象.
            像(3/5)这样的分数由两部分组成,左边的值称作分子,也可以是任意整数.右边的值称为分母,可以是任意大于0的整数(负的分数带有负的分子)
            尽管可以用浮点数来近似表示分数,但此希望能精确到表示分数的值.
            
        在Python中定义新类的做法是,提供一个类名以及一整套与函数定义语法类似的方法定义,以下是一个方法定义框架.
        class Fraction:
        
        # 方法定义:
            所有的类都应该首先提供构造方法,构造方法定义了数据对象的创建方式.
            要创建一个Fraction对象,需要提供分子和分母两部分数据.
            在Python中,构造方法总是命名为__init__(即在init的前后分别有两个下划线)
            
            class Fraction:
                def __init__(self,top,bottom):
                    self.num = top
                    self.den = bottom
                    
            * 形式参数列表包含3项.self是一个总是指向对象本身的特殊参数,它必须是第一个形式参数.

            然而,在调用方法时,从来不需要提供相应的实际参数.
            如前所述,分数需要分子与分母两部分状态数据.构造方法中的self.num定义了Fraction对象有一个叫作num的内部数据对象作为其状态的一部分.
            self.den定义了分母.这两个实际参数的值在初始化时赋给了状态,使得新创建的Fraction对象能够知道其初始值.
            要创建Fraction类的实例,必须调用构造方法,使用类名并且传入状态的实际值就能完成调用(* 不要直接调用__init__)
            
            myfraction = Fraction(3,5) # 创建了一个对象,名为myfraction,值为3/5
            
            如果直接进行打印对象,Fraction类的对象myfraction并不知道如何响应打印请求,
            print函数要求对象将自己转换成一个可以被写到输出端的字符串,
            myfraction唯一能做的就是显示储存在变量中的实际引用(地址本身).
            这不是我们想要的结果.
            
            有两种方法可以解决这个问题.
            一种是定义一个show方法,使得Fraction对象能够将自己作为字符串来打印.

            # show方法:

                class Fraction:
                    def __init__(self,top,bottom):
                        self.num = top
                        self.den = bottom
                    
                    def show(self):
                        print(self.num,'/',self.den)
                    
                if __name__ == '__main__':
                    myfraction = Fraction(3,5)
                    print(myfraction.show)
                
                
            # 3.0
            # <bound method Fraction.show of <__main__.Fraction object at 0x7f5370d0dfa0>>
    
            其二,Python的所有类都提供了一套标准方法,但是可能没有正常工作,其中之一就是将对象转换成字符串的方法__str__方法.
            这个方法的默认实现是像我们之前所见的那样返回实例的地址字符串.
            我们需要做的是为这个方法提供一个'更好'的实现,即重写默认实现,或者说重新定义该方法的行为.

            为达到这一目标,仅需定义一个名为__str__的方法,并且提供新的实现,
            除了特殊参数self之外,该方法定义不需要其他信息.
            新的方法通过将两部分内部状态数据转换成字符串并在它们之间插入字符/来将分数对象转换成字符串.
            一旦要求Fraction对象转换成字符串,就会返回结果.
            * 注意该方法的各种用法

            # __str__方法:

                class Fraction:
                    def __init__(self,top,bottom):
                        self.num = top
                        self.den = bottom

                    def __str__(self):
                        return str(self.num) + '/' + str(self.den)

                if __name__ == '__main__':
                    myf = Fraction(3,5)
                    print(myf)
                    print("I ate",myf,"of the pizza")
                    print(myf.__str__())
                    print(str(myf))


                # 3/5
                # I ate 3/5 of the pizza
                # 3/5
                # 3/5


            可以重写Fraction类中的很多其他方法,其中最重要的一些是基本的数学运算.
                class Fraction:
                    def __init__(self,top,bottom):
                        self.num = top
                        self.den = bottom

                if __name__ == '__main__':
                    f1 = Fraction(1,4)
                    f2 = Fraction(1,2)

                    print(f1 + f2)


                # print(f1 + f2)
                # TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'

            我们想创建两个Fraction对象,然后将它们相加,会出现错误,会发现加号无法处理Fraction的操作数

            可以通过重写Fraction类的__add__方法来修正这个错误.
            该方法需要两个参数,地一个仍然是self,第二个代表了表达式中的另一个操作数.
            # f1.__add__(f2)
            以上代码会要求Fraction对象f1将Fraction对象f2加到自己的值上.
            可以将其写成标准表达式: f1 + f2

            如两个分数需要有相同的分母才能相加,确保分母相同最简单的方法是使用两个分母等乘积作为分母

            a/b + c/d = ad/bd + cb/bd = ad+cb/bd

            __add__方法返回一个包含分子很分母的新Fraction对象,可以利用这一方法来编写标准的分数数学表达式,将加法结果赋给变量,并打印结果.
            值得注意的是,\这个符号称作续行符.当一条Python语句被分成多行时,需要用到续行符.

                class Fraction:
                    def __init__(self,top,bottom):

                        self.num = top
                        self.den = bottom

                    def __str__(self):
                        return str(self.num) + '/' + str(self.den)

                    def __add__(self,otherfraction):
                        newnum = self.num * otherfraction.den + \
                                    self.den * otherfraction.num
                        newden = self.den * otherfraction.den

                        return Fraction(newnum,newden)


                if __name__ == '__main__':
                    f1 = Fraction(1,4)
                    f2 = Fraction(1,2)
                    f3 = f1 + f2
                    print(f3)

                # 6/8


            虽然这一方法能够与我们预想的一样执行加法运算,但还有一处可以改进,1/4+1/2的确等于6/8,但不是最简分数.最好的表达应该是3/4
            为了保证结果总是最简分数,需要一个知道如何化简分数的辅助方法.
            该方法需要寻找分子和分母的最大公因数,然后将分子和分母分别处以最大公因数,最后的结果就是最简分数.

            * 要寻找最大公因数,最著名的方法就是欧几里得算法,欧几里得算法指出,
            对于整数m和n,如果m能被n整除,那么它们的最大公因数就是n.
            然而,如果m不能被n整除,那么结果是n与m除以n的余数的最大公因数.

            而以下代码提供了一个迭代实现,注意,这种实现只有在分母为正的时候才有效.
            对于Fraction类,这是可以接受的,因为之前已经定义过,负的分数带有负的分子,其分母为正.
            # gcd函数:
                def gcd(m,n):
                    while m%n != 0:
                        oldm = m
                        oldn = n

                        m = oldn
                        n = oldm%oldn

                    return n

            现在可以利用这个函数来化简分数,为了将一个分数转化成最简形式,需要将分子和分母都除以它们的最大公因数.
            对于分数6/8,最大公因数是2,因此,将分子和分母都除以2,以便得到3/4.

            # 改良版__add__方法:

                from math import gcd

                class Fraction:
                    def __init__(self, top, bottom):
                        self.num = top
                        self.den = bottom

                # from math import gcd math模块中gcd函数的实现细节
                    # def gcd(m, n):
                    #     while m % n != 0:
                    #         oldm = m
                    #         oldn = n
                    #
                    #         m = oldn
                    #         n = oldm % oldn
                    #
                    #     return n

                    def __str__(self):
                        return str(self.num) + '/' + str(self.den)

                    def __add__(self, otherfraction):
                        newnum = self.num * otherfraction.den + \   # \这个符号称作续行符.当一条Python语句被分成多行时,需要用到续行符
                                    self.den * otherfraction.num
                        newden = self.den * otherfraction.den
                        common = gcd(newnum, newden)

                        return Fraction(newnum // common, newden // common)


                    if __name__ == '__main__':
                        f1 = Fraction(1, 4)
                        f2 = Fraction(1, 2)
                        f3 = f1 + f2
                        print(f3)

            Fraction对象现在有两个非常有用的方法,为了允许两个分数互相比较,还需要添加一些方法.
            假设有两个Fraction对象,f1和f2.
            只有在它们是同一个对象得引用时,f1 == f2才为True.这被称为浅相等,
            在当前实现中,分子和分母相同的两个不同的对象是比相等的.
            通过重写__eq__方法,可以建立深相等----根据值来判断相等,而不是根据引用.
            __eq__是又一个在任意类中都有的标准方法.
            它比较两个对象,并且在它们的值相等时返回True,否则返回False.

            在Fraction类中,可以通过统一两个分数的分母并比较分子来实现__eq__方法,
            * 需要注意的是,其他的关系运算符也可以被重写.
            例如__le__方法提供判断小于等于的功能.

                def __eq__(self,other):
                    firstnum = self.num * other.den
                    secondnum = other.num * self.den

                    return firstnum == secondnum

            Fraction类的完整实现:

                from math import gcd

                class Fraction:
                    def __init__(self,top,bottom): # 构造方法,对象初始化.
                        self.num = top
                        self.den = bottom

                    def __str__(self):  #__str__方法,就是将对象转换成字符串的方法.
                        return str(self.num) + "/" + str(self.den)

                    def show(self):
                        print(self.num,"/",self.den)

                    def __add__(self, otherfraction):   #__add__方法返回一个包含分子很分母的新Fraction对象.
                        newnum = self.num * otherfraction.den + \
                                    self.den * otherfraction.num
                        newden = self.den * otherfraction.den
                        common = gcd(newnum,newden)

                        return Fraction(newnum // common,newden // common)
                    def __eq__(self,other):     # __eq__方法,它比较两个对象,并且在它们的值相等时返回True,否则返回False.
                        firstnum = self.num * other.den
                        secondnum = self.num * other.den

                        return firstnum == secondnum

                if __name__ == '__main__':
                    f1 = Fraction(1, 4)
                    f2 = Fraction(1, 2)
                    f3 = f1 + f2
                    print(f3)
                    print(f1.show())
                    print(f2.show())
                    print(f1.__str__(), '+', f2.__str__(), '=', f3)



                # 3/4
                # 1 / 4
                # None
                # 1 / 2
                # None
                # 1/4 + 1/2 = 3/4

        继承:逻辑门与电路：
            继承使一个类与另一个类相关联,就像人们相互联系一样.
            孩子从父母那里继承了特征.与之相似,Python中的子类可以从父类继承特征数据和行为.
            父类也称为超类.

            Python集合类{有序集合[[列表,list],"字符串,char[character string]",(元组,tuple)],无序集合[{字典dict}]}

            内建的Python集合类以及它们的相互关系,我们将这样的关系结构称为继承层次结构.
            举例来说,列表是有序集合的子,因此将列表称为子,有序集合成为父(或者分别称为子类列表和超类序列).
            这种关系通常被称为IS-A关系(IS-A意即列表是一个有序集合).
            这意味着,列表从有序集合继承了重要的特征,也就是内部数据的顺序以及诸如拼接,重复和索引等方法.

            列表，字符串和元组都是有序集合,它们都继承了共同的数据组织和操作,
            不过,根据数据是否同类以及集合是否可修改,它们彼此又有区别,子类从父类继承共同的特征,但是通过额外的特征彼此区分.

            通过将类组织成继承层次结构,面向对象编程语言使以前编写的代码得以扩展到新的应用场景中,
            此外,这种结构有助于更好地理解各种关系,从而更高效地构建抽象表示.

            为了更近一步探索这个概念,构建一个模拟程序,用于模拟数字电路.
            逻辑门是这个模拟程序的基本构造单元,它们代表其输入和输出之间的布尔代数关系.
            一般来说,逻辑门都有单一的输出,输出值取决于提供的输入值.

            与门(AND gate)有两个输入,每一个都是0或1(分别代表False和True).
            如果两个输入都是1,那么输出就是1;如果至少有一个输入是0,那么输出就是0.
            或门(OR gate)同样也有两个输入,当至少有一个输入为1时,输出就为1;当两个输入都是0时,输出是0.
            非门(NOT gate)与其它两种逻辑门不同,它只有一个输入,输出刚好与输入相反.
            如果输入是0,输出就是1,反之,如果输入是1,输出就是0.

            与门(and),或门(or),非门(not).

            通过不同的模式将这些逻辑门组合起来并提供一系列输入值,可以构建具有逻辑功能的电路.
            为了实现电路,首先需要构建逻辑门的表示,可以轻松地将逻辑门组织成类的继承层次结构,

            logicGate = [['两个输入的逻辑门', ['BinaryGate', ['与门', '或门']]], ['一个输入的逻辑门', ['UnaryGate', ['非门']]]]

            解析:
                LogicGate列表代表逻辑门的通用特性:逻辑门的字符串和一个输出.
                将一层列表逻辑门分成两种:有一个输入的逻辑门和有两个输入的逻辑门的列表
                BinaryGate字符串所在的列表中有与门(and)和或门(or),为两个输入的逻辑门
                UnaryGate字符串所在的列表中有非门(not),为一个输入的逻辑门


            现在开始通过实现最通用的类LogicGate来实现这些类.
            所有逻辑门还需要能够知道自己的输出值,这就要求逻辑门能够根据当前的输入值进行合理的逻辑运算,
            为了生成结果,逻辑门需要知道自己对应的逻辑运算是什么,在意味着需要调用一个方法来进行逻辑运算.
            超类LogicGate:
                class LogicGate:
                    def __init__(self,n):
                        self.label = n
                        self.output = None

                    def getLabel(self):
                        return self.label

                    def getOutput(self):
                        self.output = self.performGateLogic()
                        return self.output

            目前还不用实现performGateLogic函数,
            因不知道每一种逻辑门将如何进行自己的逻辑运算,这些细节会交由继承层次结构中的每一个逻辑门来实现.
            这是一种在面向对象编程中非常强大的思想----我们创建了一个方法,而代码还不存在.
            参数self是指向实际调用方法的逻辑门对象的引用.任何添加到继承层次结构中的新逻辑门都仅需要实现之后会被调用的performGateLogic函数.
            一旦实现完成,逻辑门可以提供运算结果.
            扩展已有的继承层次结构并提供使用新类所需的特定函数,这种能力对于重用代码来说非常重要.

            我们依据输入的个数来为逻辑门分类,与门和或们有两个输入,非门只有一个输入.
            BinaryGate 是LogicGate的一个子类,并且有两个输入.
            UnaryGate 同样是LogicGate的子类,但是仅有一个输入,在计算机电路设计中,这些输入被称为"引脚"(pin),我们在实现中也使用这一术语.

            BinaryGate类:
                class BinaryGate(LogicGate):
                    def __init__(self,n):
                        super().__init__(n)

                        self.pinA = None
                        self.pinB = None
                    def getPinA(self):
                        return int(input("Enter Pin A input for gate" + \
                                            self.getLabel() + "-->"))
                    def getPinB(self):
                        return int(input("Enter Pin B input for gate" + \
                                            self.getLabel() + "-->"))

            UnaryGate类:
                class UnaryGate(LogicGate):
                    def __init__(self,n):
                        super().__init__(n)

                        self.pin = None

                    def getPin(self):
                        return int(input("Enter Pin input for gate" + \
                                            self.getLabel() + "-->"))

            BinaryGate类 and UnaryGate类 两个类的构造方法首先使用super函数来调用其父类的构造方法.
            当创建BinaryGate类得实例时,首先要初始化所有从LogicGate中继承来的数据项,在这里就是逻辑门.
            接着,构造方法添加两个输入(pinA and pinB);
            这是在构建类继承层次结构时常用的模式.子类的构造方法需要先调用父类的构造方法,然后再初始化自己独有的数据.

            BinaryGate类增添的唯一行为就是取得两个输入值,由于这些值来自于外部,因此通过一条输入语句来要求用户提供.
            UnaryGate类也有类似的实现,不过它只有一个输入.

            有了不同输入个数的逻辑门所对应的通用类之后,就可以为有独特行为的逻辑门构建类，
            例如,由于与门需要两个输入,因此AndGate是BinaryGate的子类,
            和之前一样,构造方法的第一行调用父类(BinaryGate)的构造方法,该构造方法又会调用它的父类(LogicGate)的构造方法.
            注意,由于继承了两个输入,一个输出和逻辑门,因此AndGate类并没有添加任何新的数据.

            AndGte类唯一需要添加的是布尔运算行为,这就是提供performGateLogic的地方.
            对与与门来说,performGateLogic首先需要获取两个输入值,然后只有在它们都为1时返回1.

            AndGate类:
                class AndGate(BinaryGate):
                    def __init__(self,n):
                        super().__init__(n)
                    def performGateLogic(self):
                        a = self.getPinA()
                        b = self.gatPinB()
                        if a == 1 and b == 1:
                            return 1
                        else:
                            return 0

            ***

            class LogicGate:
                def __init__(self, n):
                    self.label = n
                    self.output = None

                def getLabel(self):
                    return self.label

                def getOutput(self):
                    self.output = self.performGateLogic()
                    return self.output


            class BinaryGate(LogicGate):
                def __init__(self, n):
                    super().__init__(n)

                    self.pinA = None
                    self.pinB = None

                def getPinA(self):
                    return int(input("Enter Pin A input for gate" + \
                                    self.getLabel() + "-->"))

                def getPinB(self):
                    return int(input("Enter Pin B input for gate" + \
                                    self.getLabel() + "-->"))


            class UnaryGate(LogicGate):
                def __init__(self, n):
                    super().__init__(n)

                    self.pin = None

                def getPin(self):
                    return int(input("Enter Pin input for gate" + \
                                    self.getLabel() + "-->"))


            class AndGate(BinaryGate):
                def __init__(self, n):
                    super().__init__(n)

                def performGateLogic(self):
                    a = self.getPinA()
                    b = self.getPinB()

                    if a == 1 and b == 1:  # 与门(and)值的判断 输入的两个值都为True时输出1,否则为0
                        return 1
                    else:
                        return 0


            class OrGate(BinaryGate):
                def __init__(self, n):
                    super().__init__(n)

                def performGateLogic(self):
                    a = self.getPinA()
                    b = self.getPinB()

                    if a == 1 or b == 1:  # 或门(or)值的判断 输入的两个值其中一个值为True时输出1,否则为0
                        return 1
                    else:
                        return 0


            class NotGate(UnaryGate):
                def __init__(self, n):
                    super().__init__(n)

                def performGateLogic(self):
                    p = self.getPin()

                    if not (p == 1):  # 非门(not)值的判断 输入一个值,对值取反,not对p == 1取反为0,如果条件为False,则取其反值,输出值为1
                        return 1
                    else:
                        return 0  # 否则if判断p == 0 时 not 取反为True 则输出值为 0


            if __name__ == '__main__':
                And = AndGate("G1")  # 与门
                print('与门(and):', And.getOutput())

                Or = OrGate("G2")  # 或门
                print('或门(or):', Or.getOutput())
                print('或门(or):', Or.getOutput())

                Not = NotGate("G3")  # 非门
                print('非门(not):', Not.getOutput())

            ***
            # Enter Pin A input for gateG1-->1
            # Enter Pin B input for gateG1-->0
            # 与门(and): 0
            # Enter Pin A input for gateG2-->1
            # Enter Pin B input for gateG2-->1
            # 或门(or): 1
            # Enter Pin A input for gateG2-->0
            # Enter Pin B input for gateG2-->0
            # 或门(or): 0
            # Enter Pin input for gateG3-->0
            # 非门(not): 1


            有了基本的逻辑门之后,便可以开始构建电路.
            为此,需要将逻辑门连接在一起,前一个的输出是后一个的输入,为了做到这一点,要实现一个叫作Connector的新类.
            Connector类并不在逻辑门的继承层次结构中.
            但是,它会使用该结构,从而使每一个连接器的两端都有一个逻辑门,这被称为HAS-A关系(HAS-A意即"有一个"),
            它在面向对象编程中非常重要,前文用(IS-A)关系来描述子类与父类的关系,
            例如UnaryGate是一个LogicGate.
            Connector与LogicGate是HAS-A关系.
            意味着连接器内部包含LogicGate类的实例,但是不在继承层次结构中,
            在设计类时,区分IS-A关系(需要继承)和HAS-A关系(不需要继承)非常重要.

            Connector类,每一个连接器对象都包含fromgate和togate两个逻辑门实例,数据值会从一个逻辑门的输出'流向'下一个逻辑门的输入.
            对setNexPin的调用,对于建立连接来说非常重要.
            需要将这个方法添加到逻辑门类中,以使togate能够选择适当的输入.
            Connector类:
                class Connector:

                def __init__(self, fgate, tgate):
                    self.fromgate = fgate
                    self.togate = tgate

                    tgate.setNextPin(self) # 这里是关键，将整个连接器作为后面端口的输入。每个与非门都定义了该方法。

                def getFrom(self):
                    return self.fromgate

                def getTo(self):
                    return self.togate

            setNextPin方法:
                 def setNextPin(self, source):
                    if self.pinA == None:
                        self.pinA = source
                    else:
                        if self.pinB == None:
                            self.pinB = source
                        else:
                            print("Cannot Connect: NO EMPTY PINS on this gate")

            在BinaryGate类中,逻辑门有两个输入,但连接器必须只连接其中一个,
            如果两个都能连接,那么默认的选择pinA,如果pinA已经有了连接,就选择pinB.
            如果两个输入都已有连接,则无法连接逻辑门.

            现在的输入来源有两个:外部以及上一个逻辑门的输出.
            这个需要对方法getPinA和getPinB进行修改.
            如果输入没有与任何逻辑门相连接(None),那就和之前一样要求用户输入.
            如果有了连接,就访问该连接并且获取fromgate的输出值.这会触发fromgate处理其逻辑.
            该过程会一直持续,直到获取所有输入并且最终的输出值成为正在查询的逻辑门的输入,
            在某种意义上,这个电路反向工作,以获得所需的输入,再计算最后的结果.

            修改后的getPinA方法:
                def getPinA(self):
                    if self.pinA == None:
                        return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
                    else:
                        return self.pinA.getFrom().getOutput()

            ***
            class LogicGate:

                def __init__(self, n):
                    self.name = n
                    self.output = None

                def getLabel(self):
                    return self.name

                def getOutput(self):
                    self.output = self.performGateLogic()
                    return self.output


            class BinaryGate(LogicGate):

                def __init__(self, n):
                    super(BinaryGate, self).__init__(n)

                    self.pinA = None
                    self.pinB = None

                def getPinA(self):
                    if self.pinA == None:
                        return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
                    else:
                        return self.pinA.getFrom().getOutput()

                def getPinB(self):
                    if self.pinB == None:
                        return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
                    else:
                        return self.pinB.getFrom().getOutput()

                def setNextPin(self, source):
                    if self.pinA == None:
                        self.pinA = source
                    else:
                        if self.pinB == None:
                            self.pinB = source
                        else:
                            print("Cannot Connect: NO EMPTY PINS on this gate")


            class AndGate(BinaryGate):  # 与门(and)

                def __init__(self, n):
                    BinaryGate.__init__(self, n)

                def performGateLogic(self):

                    a = self.getPinA()
                    b = self.getPinB()
                    if a == 1 and b == 1:
                        return 1
                    else:
                        return 0


            class OrGate(BinaryGate):  # 或门(or)

                def __init__(self, n):
                    BinaryGate.__init__(self, n)

                def performGateLogic(self):

                    a = self.getPinA()
                    b = self.getPinB()
                    if a == 1 or b == 1:
                        return 1
                    else:
                        return 0


            class UnaryGate(LogicGate):

                def __init__(self, n):
                    LogicGate.__init__(self, n)

                    self.pin = None

                def getPin(self):
                    if self.pin == None:
                        return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
                    else:
                        return self.pin.getFrom().getOutput()

                def setNextPin(self, source):
                    if self.pin == None:
                        self.pin = source
                    else:
                        print("Cannot Connect: NO EMPTY PINS on this gate")


            class NotGate(UnaryGate):  # 非门(not)

                def __init__(self, n):
                    UnaryGate.__init__(self, n)

                def performGateLogic(self):
                    if self.getPin():
                        return 0
                    else:
                        return 1


            class Connector:

                def __init__(self, fgate, tgate):
                    self.fromgate = fgate
                    self.togate = tgate

                    tgate.setNextPin(self) # 这里是关键，将整个连接器作为后面端口的输入。每个与非门都定义了该方法。

                def getFrom(self):
                    return self.fromgate

                def getTo(self):
                    return self.togate


            if __name__ == '__main__':
                g1 = AndGate("G1")
                g2 = AndGate("G2")
                g3 = OrGate("G3")
                g4 = NotGate("G4")
                c1 = Connector(g1, g3)
                c2 = Connector(g2, g3)
                c3 = Connector(g3, g4)

                print(g4.getOutput())


            ***
            # Enter Pin A input for gate G1-->0
            # Enter Pin B input for gate G1-->1
            # Enter Pin A input for gate G2-->1
            # Enter Pin B input for gate G2-->1
            # 0

            两个与门(g1和g2)的输出与或门(g3)的输入相连接,或门的输出又与非门(g4)的输入相连接.
            非门的输出就是整个电路的输出.


            # 第一个相对比较好理解，第二个理解也还好，书中由于篇幅限制，没有写全。
            # 但自己写真心写不出来，这个一种反向思考的思路，只能看懂


            小结：
                计算机科学是研究如何解决问题的学科.
                计算机科学利用抽象这一工具来表示过程和数据.
                抽象数据类型通过隐藏数据的细节来使程序员能够管理问题的复杂度.
                Python是一门强大、易用的面向对象编程的语言.
                列表、元祖以及字符串使Python的内建有序集合.
                字典和集是无序集合.
                类使得程序员能够实现抽象数据类型.
                程序员既可以重写标准方法，也可以构建新的方法.
                类可以通过继承层次结构来组织.
                类的构建方法总是先调用其父类的构建方法，然后才处理自己的数据和行为.

            关键术语:
                HAS-A关系             IS-A关系             self
                超类                  抽象                 编程
                抽象数据类型           独立与实现            对象
                方法                  封装                 格式化运算符
                格式化字符串           过程抽象              继承
                继承层次结构           接口                 可计算
                可修改性               类                  列表
                列表解析式             模拟                 浅相等
                深相等                数据抽象              数据结构
                数据类型               算法                 提示符
                信息隐藏               异常                 真值表
                子类                  字典                 字符串

'''
