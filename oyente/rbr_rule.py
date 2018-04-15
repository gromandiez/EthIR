#Pablo Gordillo

'''
RBRRule class represents the rules of the transaction system.
Each rule contains:
 * identifier

'''

class RBRRule:
    def __init__(self,blockId,typeBlock):
        self.blockId = blockId

        if typeBlock == "block":
            self.rule_name = "block"+str(blockId)
        else:
            self.rule_name = "jump"+str(blockId)

        self.arg_input = 0
        self.arg_global = []
        self.arg_local = []
        self.arg_ret = []
        self.guard=""
        self.instr=[]
        self.rbr_type = typeBlock

    def get_guard(self):
        return self.guard

    def set_guard(self, guard):
        self.guard = guard

    # def add_guard(self, guard):
    #     self.guard.append(guard)

    def get_Id(self):
        return self.blockId

    def set_Id(self, b_id):
        self.blockId = b_id

    def get_instructions(self):
        return self.instr

    def set_instructions(self, instr):
        self.instr = instr

    def add_instr(self, instr):
        self.instr.append(instr)

    def get_type(self):
        return self.rbr_type

    def get_rule_name(self):
        return self.rule_name

    def write_rule(self, fd):
        pass

    def get_index_invars(self):
        return self.arg_input

    def set_index_input(self,num):
        self.arg_input = num

    def built_input_vars(self):
        in_vars = []
        for i in xrange(0,self.arg_input):
            var = "i("+i+")"
            in_vars.append(var)
        return in_vars

    def get_args_local(self):
        return self.arg_local

    def set_args_local(self,ls):
        self.arg_local = ls

    def add_arg_local(self,l):
        if l not in self.arg_local:
            self.arg_local.append(l)
        
    def display(self):
        print self.rule_name+"("+str(self.arg_input)+", "+ str(self.arg_global)+", "+ str(self.arg_ret) +")=>"

        if self.guard != [] :
            print "\t"+self.guard

        for instr in self.instr:
            print "\t"+instr
