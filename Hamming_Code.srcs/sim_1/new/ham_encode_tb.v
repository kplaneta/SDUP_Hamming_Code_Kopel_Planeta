`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06.06.2018 13:43:05
// Design Name: 
// Module Name: ham_encode_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module ham_encode_tb();

reg reset;
reg clk;
reg[10:0] in;
wire[14:0] out;

ham_encode hamming(clk, in, out, reset);

 // Reset stimulus
 initial
 begin
  reset = 1'b1;
 #5 reset = 1'b0;
 end
 
 // Clocks stimulus
 initial
 begin
  clk = 1'b0; //set clk to 0
 end
 always
 begin
 #5 clk = ~clk; //toggle clk every 5 time units
 end

//Stimuli signals
initial
begin
    in <= 11'b00000000011;
    #9 in <= 11'b00000000111;
    #19 in <= 11'b00000001111;
    #29 in <= 11'b00000000001;
    #39 reset <= 1'b1;
    #41 reset <= 1'b0;
    #59 in <= 11'b00000010001;
    #69 in <= 11'b00101110101;
end

endmodule