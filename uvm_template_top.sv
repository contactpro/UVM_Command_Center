// 
// Author: 
// Filename: uvm_template_top.sv  
// Version: Demo       
// Description: testbench top template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_MEM_TB_TOP
`define PKT_MEM_TB_TOP

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.7/uvm_template_interface.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.7/uvm_template_env.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.7/uvm_template_base_test.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.7/uvm_template_wr_rd_test.sv"

module uvm_template_top;
  timeprecision  1ps;
  timeunit       1ns;
  
  //clock and reset signal declaration
  bit clk;
  bit reset;
  
  bit time_event_0ns;
  bit time_event_1ns;
  bit time_event_5ns;
  bit time_event_10ns;
  bit time_event_100ns;
  bit time_event_1000ns;
  bit time_event_10000ns;
  
  bit disable_message_flag_0ns;
  bit disable_message_flag_1ns;
  bit disable_message_flag_5ns;
  bit disable_message_flag_10ns;
  bit disable_message_flag_100ns;
  bit disable_message_flag_1000ns;
  bit disable_message_flag_10000ns;
  
  // interface instance
  my_if intf(clk,reset);
  
  // memory DUT instance
  uvm_template_memory_dut DUT (
    .clk(intf.clk),
    .reset(intf.reset),
    .addr(intf.addr),
    .wr_en(intf.wr_en),
    .rd_en(intf.rd_en),
    .wdata(intf.wdata),
    .rdata(intf.rdata)
   );  
  
  
  // clock generation
  always #5ns clk = ~clk;
  
  // reset generation
  initial begin
    reset = 1;
    #30ns reset = 0;
  end
  
  // Simulation Time Progress Tracker EVENT BIT initialization. 
  initial begin
    time_event_0ns = 0;  	
    time_event_1ns = 0;
    time_event_5ns = 0;
    time_event_10ns = 0;
    time_event_100ns = 0;
    time_event_1000ns = 0;
    time_event_10000ns = 0;
    disable_message_flag_0ns = 0;
    disable_message_flag_1ns = 0;
    disable_message_flag_5ns = 0;
    disable_message_flag_10ns = 0;
    disable_message_flag_100ns = 0;
    disable_message_flag_1000ns = 0;
    disable_message_flag_10000ns = 0;
  end
  
  // Simulation Time Progress Tracker EVENT BIT SET.
  always @(posedge clk)
  begin
  	if($time == 0ns) time_event_0ns = 1;
  	if($time > 1ns) time_event_1ns = 1;
   	if($time > 5ns) time_event_5ns = 1;
    if($time > 10ns) time_event_10ns = 1;
    if($time > 100ns) time_event_100ns = 1;
    if($time > 1000ns) time_event_1000ns = 1;
    if($time > 10000ns) time_event_10000ns = 1;
  end				 		

  // Simulation Time Progress Tracker Messages.
  always @(posedge clk)
  begin
  	if((time_event_0ns == 1) && (disable_message_flag_0ns == 0)) begin
  		disable_message_flag_0ns = 1; 
  	  `uvm_info("TOP TIME TRACKER","At ZERO Simulation Time at 0ns ",UVM_MEDIUM)
   	end  	
  	if((time_event_1ns == 1) && (disable_message_flag_1ns == 0)) begin
  		disable_message_flag_1ns = 1; 
  	  `uvm_info("TOP TIME TRACKER","Simulation Time Progress at 1ns ",UVM_MEDIUM)
   	end
  	if((time_event_5ns == 1) && (disable_message_flag_5ns == 0)) begin
   		disable_message_flag_5ns = 1;  		
  	  `uvm_info("TOP TIME TRACKER","Simulation Time Progress at 5ns ",UVM_MEDIUM)
   	end
   	if((time_event_10ns == 1) && (disable_message_flag_10ns == 0)) begin
  		disable_message_flag_10ns = 1;    		
  	  `uvm_info("TOP TIME TRACKER","Simulation Time Progress at 10ns ",UVM_MEDIUM)
   	end
  	if((time_event_100ns == 1) && (disable_message_flag_100ns == 0)) begin
  		disable_message_flag_100ns = 1;   		
  	  `uvm_info("TOP TIME TRACKER","Simulation Time Progress at 100ns ",UVM_MEDIUM)
   	end
   	if((time_event_1000ns == 1) && (disable_message_flag_1000ns == 0)) begin
  		disable_message_flag_1000ns = 1;    		
  	  `uvm_info("TOP TIME TRACKER","Simulation Time Progress at 1000ns ",UVM_MEDIUM)
   	end
    if((time_event_10000ns == 1) && (disable_message_flag_10000ns == 0)) begin
    	disable_message_flag_10000ns = 1; 
  	  `uvm_info("TOP TIME TRACKER","Simulation Time Progress at 10000ns ",UVM_MEDIUM)
   	end  	     	 	   	  	
  end				 

  // enabling the wave dump
  initial begin 
    // uvm_config_db#(virtual my_if)::set(null,"uvm_test_top.env.agnt+","vif",intf);
    // enable wave dump
    $dumpfile("dump.vcd"); 
    $dumpvars;
  end
  
  // passing the interface handle to 
  // the lower heirarchy using set method   
  // calling test 
  //
  // The command line argument (+UVM_TESTNAME=SOME_NEW_TESTNAME) 
  // takes precedence over the test name passed 
  // via the run_test(SOME_TESTNAME) function argument.
  // 
  initial begin 
  	// Print the simulation time in ns by default
    $timeformat(-9, 0, "", 11);  // units, precision, suffix, min field width
  	`uvm_info("TOP_TB","Executing  runtest  in TOP_TB initial block . . .",UVM_MEDIUM)
    uvm_config_db#(virtual my_if)::set(null,"*","vif",intf); 	
    // run_test("uvm_template_base_test");
    // run_test("uvm_template_base_test");
    // run_test("uvm_template_base_test");
    run_test();
  end
  
endmodule: uvm_template_top

`endif
