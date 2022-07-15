using System;
using System.Threading;

namespace Mycobot.csharp
{
    class Test
    {
        static void Main(string[] args)
        {
            MyCobot mc = new MyCobot("COM3");
            //MyCobot mc2 = new MyCobot("COM4");
            //Raspberry Pi robotic arm serial port name: / dev / ttyAMA0
            
            mc.Open();

            //After Windows opens the serial port, you need to wait for 5s.
            //After Windows opens the serial port, the basic at the bottom will restart.
            Thread.Sleep(5000);
            
            //Console.WriteLine("...Returning Cobot to Origin");
            int[] angles = new[] {0, 0, 0, 0, 0, 0};
            mc.SendAngles(angles, 80);
            Thread.Sleep(5000);

            //Console.WriteLine("...Performing Movement");
            
            rockBackAndForthForever(mc);

            /*Console.WriteLine("Gertrude:");
            var recAngles = mc.GetAngles();
            foreach (var v in recAngles)
            {
               Console.WriteLine(v);
            }*/

            mc.Close();
        }

        public static void shakeHead(MyCobot mc)
        {
            //Moves the Cobot into a position where the head can face the user.
            int[] angles = new[] { 180, 0, 0, 0, 0, 0 };
            mc.SendAngles(angles, 80);
            Thread.Sleep(4000);

            //"Shakes" the cobot's head
            mc.SendOneAngle(5, 0, 100);
            Thread.Sleep(500);
            mc.SendOneAngle(5, -40, 100);
            Thread.Sleep(500);
            mc.SendOneAngle(5, 40, 100);
            Thread.Sleep(500);
            mc.SendOneAngle(5, 0, 100);
            Thread.Sleep(500);
        }

        public static void rockBackAndForthForever(MyCobot mc)
        {
            double x = 0.0;
            int nextAngle = 0;
            int currentAngleJoint1 = 0;

            int[] currentAngles = mc.GetAngles();
            if (currentAngles.Length != 0)
            {
                currentAngleJoint1 = currentAngles[0];
            }

            while (true)
            {
                while (x >= -0.98)
                {
                    nextAngle = (int)((180 / Math.PI) * Math.Asin(x));
                    mc.SendAngles(new int[] { currentAngleJoint1, -nextAngle, nextAngle, -nextAngle, 0, 0 }, 100);
                    Thread.Sleep(100);

                    x -= 0.02;
                }


                while (x <= 0.98)
                {
                    nextAngle = (int)((180 / Math.PI) * Math.Asin(x));
                    mc.SendAngles(new int[] { currentAngleJoint1, -nextAngle, nextAngle, -nextAngle, 0, 0 }, 100);
                    Thread.Sleep(100);

                    x += 0.02;
                }
            }
        }

        public static void rockBackAndForth(MyCobot mc)
        {
            double x = 0.0;
            int nextAngle = 0;
            int currentAngleJoint1 = 0;

            int[] currentAngles = mc.GetAngles();
            if (currentAngles.Length != 0)
            {
                currentAngleJoint1 = currentAngles[0];
            }

            while (x >= -0.98)
            {
                nextAngle = (int)((180 / Math.PI) * Math.Asin(x));
                mc.SendAngles(new int[] { currentAngleJoint1, -nextAngle, nextAngle, -nextAngle, 0, 0 }, 100);
                Thread.Sleep(100);

                //Console.WriteLine("x: " + x + " Arcsine(-x):" + Math.Asin(x) + " ...in Degrees: " + nextAngle);

                x -= 0.02;
            }


            while (x <= 0.98)
            {
                nextAngle = (int)((180 / Math.PI) * Math.Asin(x));
                mc.SendAngles(new int[] { currentAngleJoint1, -nextAngle, nextAngle, -nextAngle, 0, 0 }, 100);
                Thread.Sleep(100);

                //Console.WriteLine("x: " + x + " Arcsine(-x):" + Math.Asin(x) + " ...in Degrees: " + nextAngle);

                x += 0.02;
            }
        }


    }
}