class HelloWorldC { 
    def main(args: Array[String]) { 
        println("Hello, world - NON SINGLETON!")
        args.foreach(println)
    }
}


object HelloWorld { 
    def main(args: Array[String]) { 
        var hw = new HelloWorldC()
        hw.main(args)
    } 
}
