// 
// Author: 
// Filename: uvm_template_interface.sv  
// Version: Demo       
// Description: interface template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
  
timeprecision  1ps;
timeunit       1ns;
  
interface my_if(input logic clk,reset);
  //declaring the signals
  logic [1:0] addr;
  logic wr_en;
  logic rd_en;
  logic [7:0] wdata;
  logic [7:0] rdata;
  
  // driver clocking block
  clocking driver_cb @(posedge clk);
    default input #1 output #1;
    output addr;
    output wr_en;
    output rd_en;
    output wdata;
    input  rdata;  
  endclocking
  
  // monitor clocking block
  clocking monitor_cb @(posedge clk);
    default input #1 output #1;
    input addr;
    input wr_en;
    input rd_en;
    input wdata;
    input rdata;  
  endclocking
  
  // driver modport
  modport DRIVER (clocking driver_cb,input clk,reset);
  
  //monitor modport  
  modport MONITOR (clocking monitor_cb,input clk,reset);
  
endinterface