'''
    Python数据结构与算法分析:

        编程是指通过编程语言将算法编码以使其能被计算机执行的过程.
        计算机中的所有数据实例均由二进制字符串来表达,
        为了赋予这些数据实际的意义,
        必须要有数据类型.
        数据类型能够帮助我们解读二进制数据的含义.
        从而使我们能从待解决问题的角度来看待数据,
        这些内建的底层数据类型(又称原生数据类型)提供了算法开发的基本单元.

    抽象数据类型:

        利用抽象来帮助自己专注于全局,从而避免迷失在众多细节中.
        过程抽象将功能的实现细节隐藏起来,从而使用户从更高的视角来看待问题,
        数据抽象的基本思想与此类似.
        抽象数据类型(简称ADT),从逻辑上描述了如何看待数据及其对应的运算而无须考虑具体实现,
        通过这样的抽象,我们对数据进行了一层封装,
        其基本思想是对封装具体的实现细节,使它们对用户不可见,这被称为信息隐藏.
        抽象数据类型的实现常被称为数据结构.
        这需要我们通过编程语言的语法结构和原生数据类性从物理的视角看待数据.
        分成这两种不同的视角有助于为问题定义复杂的数据模型,而无须考虑模型的实现细节.
        这便提供了一个独立于实现的数据视角.
    为何要学习算法?

        计算机科学家通过经验来学习:
        观察他人如何解决问题,然后亲自解决问题,接触各种问题解决技巧并学习不同的算法的设计方法,
        有助于解决新的问题,通过学习一系列不同的算法,可以举一反三,从而在遇到类似的问题时,能够快速的加以解决.
    Python数据:

        在Python以及其他所有面向对象编程语言中,
        类都是对数据的构成(状态)以及数据能做什么(行为)的描述.
        由于类的使用者只能看到数据项的状态和行为,因此类与抽象数据类型是相似的,
        在面向对象范式中,数据项被称为对象,一个对象就是类的一个实例.

    内建原子数据类型:
        Python有两大内建数据类实现了整数类型和浮点数类型,
        相应的Python类就是:
            int and float
        标准的数学运算符:
            即+,-,*,/,**,可以和能够改变运算符优先级的括号一起使用.
        其他运算符:
            %(取余/取模),//(整除)
        bool类实现对表达式真值非常有用的布尔数据类型:
            布尔对象可能的状态值是:
                True(1)
                False(0)
            布尔对象也可用来运算和比较.

            关系运算符and逻辑运算符:
                <   (小于)
                >   (大于)
                =   (等于)
                ==  (赋值)
                >=  (大于等于)
                <=  (小于等于)
                !=  (不等于)
                and (两个运算数都为True时结果为True)
                or  (某一个运算符为True时结果为True)
                not (对真值取反,False变为True,True就变为False)
    内建集合数据类型:
        除了数值类and布尔类,Python还有内建集合类.
        列表,字符串,元组是概念上非常相似的有序集合,
        集(set)and字典是无序集合
            列表(list):
                列表是零个或多个指向Python对象的引用的有序集合[]
                列表是异构的,这意味着其指向的数据对象不需要都是同一个类,并且这一集合可以赋值给一个变量.
                Python计算一个列表时,这个列表自己会被return

                可用于任意Python序列的运算:
                    索引 []   (取序列中的某个元素)
                    连接 +    (将序列连接在一起)
                    重复 *    (重复N次连接)
                    成员 in   (询问序列中是否有某元素)
                    长度 len  (询问序列的元素个数)
                    切片 [:]  (取出序列的一部分)

                Python列表提供的方法:
                    append  | list.append(item)     (在列表末尾添加一个新元素)
                    insert  | list.insert(i,item)   (在列表的第i个位置插入一个元素)
                    pop     | list.pop()            (删除并返回列表中最后一个元素)
                    pop     | list.pop(i)           (删除并返回列表中第i个位置的元素)
                    sort    | list.sort()           (将列表元素排序)
                    reverse | list.reverse()        (将列表元素倒序排列)
                    del     | del list[i]           (删除列表中第i个位置的元素)
                    index   | list.index(item)      (返回item第一次出现时的下标)
                    count   | list.count(item)      (返回item在列表中出现的次数)
                    remove  | list.remove(item)     (从列表中移除第一次出现的item)
                × pop()这样的方法在返回值的同时也会修改列表的内容,
                * reverse()等方法则仅修改列表而不会返回任何值,
                * pop()默认返回并删除列表的最后一个元素,但是也可以用来返回并删除特定的元素.
                # 这些方法默认下标从0开始.
                * myList.append(False)
                # 可以读作为'请求myList调用append方法并将False这一值传给它'

                range()方法会生成一个代表值序列的范围对象,使用list函数,能够以列表形式看到范围对象的值.

            字符串(char[character string]):
                字符串是零个或多个字母,数字,其他符号的有序集合.
                这些字母,数字,其他符号被称为字符(character).
                常量字符串值通过引号(单引号或者双引号均可)与标识符进行区分
                由于字符串是序列,因此所有的序列运算符都能用于字符串.

                Python字符串提供的方法:
                    center   | string.center(w)      (返回一个字符串,原字符串居中,使用空格填充新字符串,使其长度为w)
                    count    | string.count(item)    (返回item出现的次数)
                    ljust    | string.ljust(w)       (返回一个字符串,将原字符串靠坐放置并填充空格至长度w)
                    rjust    | string.rjust(w)       (返回一个字符串,将原字符串靠右放置并填充空格至长度w)
                    lower    | string.lower()        (返回均为小写字母的字符串)
                    upper    | string.upper()        (返回均为大写字母的字符串)
                    find     | string.find(item)     (返回item第一次出现时的下标)
                    split    | string.split(char)    (在char位置将字符串分割成子串)

                * split()在处理数据的时候非常有用,split()接受一个字符串,并且返回一个由分隔字符作为分割点的字符串列表.
                * 列表and字符串的主要区别在于,列表能够被改变,字符串则不能,列表的这一特性被称为可修改性.
                * 列表具有可修改性,字符串则不具有.
                * 因都是异构数据序列,因此元组与列表非常相似,区别于,元组and字符串一样是不可修改的.
                * 元组通常写成由括号包含并且1以逗号分隔的一系列值，与序列一样,元组允许之前描述的任意操作.

            集(set):
                集(set)是由多个或多个不可修改的Python数据对象组成的无序集合,
                集不允许重复元素,并且写成由花括号包含,以逗号分隔的一系列值.
                空集由set()来表示.集是异构的.
                set = {}
                # 尽管集是无序的,但它还是支持一些运算的.

                Python集支持的运算:
                    成员  in                  (询问集中是否有某元素)
                    长度  len                 (获取集的元素个数)
                    |    set | otherset      (返回一个包含set与otherset所有元素的新集)
                    &    set & otherset      (返回一个包含set与otherset共有元素的新集)
                    -    set - otherset      (返回一个集,其中包含只出现在set中的元素)
                    <=   set <= otherset     (询问set中的所有元素是否都在otherset中)
                Python集提供的方法:
                    union        | set.union(otherset)         (返回一个包含set和otherset所有元素的集)
                    intersection | set.intersection(otherset)  (返回一个仅包含两个集共有元素的集)
                    difference   | set.difference(otherset)    (返回一个集,其中仅包含只出现在set中的元素)
                    issubset     | set.issubset(otherset)      (询问set是否为otherset的子集)
                    add          | set.add(item)               (向set添加一个元素)
                    remove       | set.remove(item)            (将item从set中移除)
                    pop          | set.pop()                   (随机移除set中的一个元素)
                    clear        | set.clear()                 (清除set中的所有元素)

            字典(dict)：
                Python集合,字典(dict),字典是无序结构,由相关的额元素对构成,其中每对元素都由一个键和一个值组成.
                这种键-值对通常写成键:值的形式.
                由{}包含的一系列以逗号分隔的键-值对表达.

                Python字典支持的运算:
                    []   | myDict[k]         (返回与k相关联的值,如果没有则报错)
                    in   | key in dict       (如果key在字典中,返回True,否则返回False)
                    del  | ael dict[key]     (从字典中删除key的键-值对)

                Python字典提供的方法:
                    keys    | dict.keys()       (返回包含字典中所有的键的dict_keys对象)
                    values  | dict.values()     (返回i包含字典中所有的值的dict_values对象)
                    items   | dict.items()      (返回包含字典中所有的键-值对的dict_items对象)
                    get     | dict.get(k)       (返回包含k对应的值,如果没有则返回None)
                    get     | dict.get(k,alt)   (返回k对应的值,如果没有则返回alt)

    Python输入与输出:
        程序经常需要与用户进行交互,以获得数据或者提供某种结果.
        input()函数接受一个字符串作为参数,由于该字符串包含有用的文本来提示用户输入,因此它经常被称为提示字符串.
        * input()函数返回的值是一个字符串,它包含用户在提示字符串后面输入的所有字符.
        * 如果需要将这个字符串转换成其他类型,必须明确地提供类型转换.

        格式化字符串:
            print()函数为输出Python程序的值提供了一种非常简便的方法,
            * 它接受零个或者多个参数,并且将单个空格作为默认分隔符来显示结果.通过设置sep这一实际参数可以改变分隔符.
            * 此外,每一次打印都默认以换行符结尾,这一行为可以通过设置实际参数end来更改.
            * 更多地控制程序的输出格式经常十分有用,Python提供了另一种叫作格式化字符串的方式.
            格式化字符串是一个模板,其中包含保持不变的单词或空格,以及之后插入的变量的占位符.
            print("%s is %d years old." % (aName,age))
            这个例子展示了一个新的字符串表达式,
            % 是字符串运算符,被称为格式化运算符.
            表达式的左边部分是模板(也叫格式化字符串)
            右边部分则是一系列用于格式化字符串的值.
            * 右边的值的个数与格式化字符串中的%的个数要一致.这些值将依次从左到右地被换入格式化字符串.

            格式化字符串可以包含一个或者多个转换声明,转换字符串告诉格式化运算符,什么类型的值会被插入到字符串中的相应位置.

            格式化字符串可用的类型声明:
                d,i     (整型)
                u       (无符号整数)
                f       (m.dddd格式的浮点数)
                e       (m.dddde+/-xx格式的浮点数)
                E       (m.ddddE+/-xx格式的浮点数)
                g       (对指数小于-4或者大于5的使用%e,否则使用%f)
                c       (单个字符)
                s       (字符串,或者任意可以通过str函数转换成字符串的Python数据对象)
                %       (插入一个常量%符号)

                * 可以在%和格式化字符之间加入一个格式化修改符.
                * 格式化修改符可以根据给定的宽度对值进行左对齐或者右对齐,也可以通过小数点之后的一些数字来指定宽度.

            格式化修改符:
                数字     |   %20d        (将值放在20个字符宽的区域中)
                -       |   %-20d       (将值放在20个字符宽的区域中,并且左对齐)
                +       |   %+20d       (将值放在20个字符宽的区域中,并且右对齐)
                0       |   %020d       (将值放在20个字符宽的区域中,并且前面补上0)
                .       |   %20.2f      (将值放在20个字符宽的区域中,并且保留小数点后2位)
                (name)  |   %(name)d    (从字典获取name键对应的值)

                × 格式化运算符的右边是将被插入的格式化字符串的一些值.
                这个集合可以是元组或字典.
                如果这个集合是元组,那么值就根据位置的次序被插入,也就是说,元组的第一个元素对应于格式化字符串中的第一个格式化字符.
                如果这个集合是字典,那么值就根据它们对应的键被插入,并且所有的格式化字符必须使用(name)修改符来指定键名.
                * Python字符串还包含了一个format()方法,该方法可以与新的Formatter类结合起来使用,从而实现复杂字符串的格式化.

    Python控制流程:
        算法需要两个重要的控制结构:迭代和分支.
        对于迭代,Python提供了while语句以及非常强大的for语句.
            while 会在给定条件为真时重复执行一段代码.
            while True:
                ...
            for 则可以很好地和Python的各种集合结合在一起使用.for语句用于遍历一个序列集合的每个成员.

            for item in [1,2,3,4,5]:
                print(item)

            for语句将列表[1,2,3,4,5]中的每一个值依次赋值给变量item,然后迭代语句就会被执行.
            * 这样的做法对任意的序列集合(列表,元组以及字符串)都有效.
            * for语句的一常见用法是在一定的值的范围内进行有限次数的迭代.

            for语句会执行print函数5次,range函数会返回一个包含序列0,1,2,3,4的范围对象,每个值都会被赋值给变量item
            Python会计算该值的平方并且打印结果.

            for i in range(5):
                print(item ** 2)

            *for语句的另一个非常有用的使用场景是处理字符串中的每一个字符.
            下面的代码段遍历一个字符串列表, 并且将每一个字符串中的每一个字符都添加到结果列表中.
            最终的结果就是一个包含所有字符串的所有字符的列表.

            wordlist = ['cat', 'dog', 'rabbit']
            letterlist = []
            for aword in wordlist:
                for aletter in aword:
                    letterlist.append(aletter)
            print(letterlist)

            # ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

        分支语句允许进行询问,然后根据结果,采取不同的行为.
        分支结构:
            if else 和 if
            以下使用if else 语句的一个简单的二元分支.
            if n < 0:
                print("Sorry, value is negative")
            else:
                print(math.sqrt(n))
            这个例子会检查n所指向的对象是否小于0,
            如果是,打印一条信息,说明是负值;如果不是,就会执行else分支来计算它的平方根.
            分支结构支持嵌套,一个问题的结果能帮助决定是否需要继续问下一个问题.

            例如,假设score是指向计算机科学考试分数的变量.
            score = int(input('int:'))
            if score >= 90:
                print('A')
            else:
                if score >= 80:
                    print('B')
                else:
                    if score >= 70:
                        print('C')
                    else:
                        if score >= 60:
                            print('D')
                        else:
                            print('F')
            解析:
                通过打印字母等级来对变量score进行分类.
                如果分数大于等于90,这一语句会打印 A;如果小于90(else),会接着问一下个问题.
                如果分数大于等于80,因为小于90,所以它介于80和89之间,那么语句会打印 B;
                可以发现,Python的缩进模式帮助我们在不需要额外语法元素的情况下有效地关联对应的if和else.

            另一种表达嵌套分支的语法是使用elif关键字,将else和下一个if结合起来,可以减少额外的嵌套层次.
            * else仍然是必需的,它用来所有分支条件都不满足的情况下提供默认分支.

            score = int(input('int:'))

            if score >= 90:
                print('A')

            elif score >= 80:
                print('B')
            elif score >= 70:
                print('C')
            elif score >= 60:
                print('D')
            else:
                print('F')

            Python也有单路分支结构,即if语句.如果条件为真,就会执行相应的代码.
            条件为假,程序会跳过if语句,执行下面的语句.

            例如:
                下面代码会首先检查变量n的值是否为负,如果为负,那么就取它的绝对值,再计算它的平方根.

                import math

                n = int(input(':'))
                if n < 0:
                    n = abs(n)
                print(math.sqrt(n))


            列表可以通过使用迭代结构和分支结构来创建,这种方式被称为列表解析式.
            通过列表解析式,可以根据一些处理和分支标准轻松的创建列表.

            例如:
                如果想创建一个包含前10个完全平方数的列表,可以使用以下的for语句.

                sqlist = []
                for x in range(1,11):
                    sqlist.append(x*x)

                print(sqlist)

                # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

                使用列表解析式,只需要一行代码即可:

                sqlist = [x * x for x in range(1, 11)]
                print(sqlist) # print()函数不算哦,我说这是一行就是一行,不要来和我理论,我会告诉你神码叫做下标,0,1,可不就是1行代码么.

                # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

            变量x会依次取由for语句指定的1到10的值,之后,计算x*x的值并将结果添加到正在构建的列表中.
            列表解析式也允许添加一个分支语句来控制添加到列表中的元素.

            例如:
                sqlist = [x*x for x in range(1,11) if x % 2 != 0]
                print(sqlist)

                # [1, 9, 25, 49, 81]

            这一列表解析式构建的列表只包含1到10中的奇数的平方数,任意支持迭代的序列都可用于列表解析式.

            例如:
                list = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
                # not (对真值取反,False变为True,True就变为False)如果ch遍历的字符串中有'aeiou'中任意一个字符出现时就将其删除掉 upper()
                print(list)

    Python异常处理:
        在编写程序时通常会遇到两种错误,第一种是语法错误,第二种是逻辑错误.
        语法错误:编写程序的语句或者表达式时出错.
        逻辑错误:
            即程序能执行完成但返回了错误的结果.这可能由于算法本身有错,或者程序员没有正确地实现算法.
            有时,逻辑错误会导致诸如除以0,越界访问列表等非常严重的情况.
            这些逻辑错误会导致运行时错误,进而导致程序终止运行,
            通常这些运行时错误被称为异常.

        许多初级程序员简单地把异常等同于引起程序终止的严重运行时错误,然而,大多数编程语言都提供了让程序员能够处理这些错误的方法.
        此外,也可以在检测到程序执行有问题的情况下自己创建异常.

        当异常发生时,称程序"跑出"异常.
        可用try语句来"处理"被抛出的异常.

        例如:
            以下代码段要求用户输入一个整数,然后从数学库(math)中调用平方根函数(sqrt)
            如果用户输入了一个大于或等于0的值,那么其平方根就会被打印出来.
            但是用户输入了一个负数,平方根函数就会报告ValueError异常.

            import math
            anumber = int(input('Please enter an integer:'))
            print(math.sqrt(anumber))

            # Traceback (most recent call last):
            #    File ... , line ..., in <module>
            # print(math.sqrt(anumber))
            # ValueError: math domain error

        可以在try语句块中调用print函数来处理这个异常.
        对应的except语句块"捕捉"到这个异常,并且为用户打印一条提示信息.

            import math
            try:
                anumber = int(input('Please enter an integer:'))
                print(math.sqrt(anumber))

            except:
                print("Bad Value for square root")
                print("Using absolute value instead")
                print(math.sqrt(abs(anumber)))  # abs()函数求绝对值

        * except会捕捉到sqrt抛出的异常并打印提示消息,然后会使用对应数字的绝对值来保证sqrt的参数非负,意味着程序并不会终止,而是继续执行后续语句.

        也可以使用raise语句来触发运行时异常,
        例如：
            可以先检查值是否为负,并在值为负时抛出异常,而不是给sqrt函数提供负数.
            下面代码段显示了创建新的RuntimeError异常的结果.
            注意,程序仍然会终止,但是导致其终止的异常是由我们自己手动创建的

            import math

            try:
                anumber = int(input(':'))
                if anumber < 0:
                    raise RuntimeError("You can't use a negative number")  # 自己手动创建的异常
                else:
                    print(math.sqrt(anumber))
            except ValueError:  # ValueError: invalid literal for int() with base 10: 'q'
                print('ValueError')

'''
