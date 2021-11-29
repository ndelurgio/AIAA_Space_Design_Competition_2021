stk.v.12.0
WrittenBy    STK_v12.0.1

BEGIN Planet

    Name		 Deimos

    BEGIN PathDescription

        CentralBody		 Deimos
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 None

            JplIndex		 -1

            JplSpiceId		 402

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		  2.4478930006618500e+06
            OrbitCrdSys		 Inertial
            OrbitCrdSysEpoch		  2.4515450000000000e+06
            OrbitMeanDist		  2.3484831253618840e+07
            OrbitEcc		  1.1557099999999999e-03
            OrbitInc		  1.7858128300000000e+00
            OrbitRAAN		  1.4803022507000000e+02
            OrbitPerLong		  1.2333509595466261e+02
            OrbitMeanLong		  4.6969355894030002e+02
            OrbitMeanDistDot		  0.0000000000000000e+00
            OrbitEccDot		  0.0000000000000000e+00
            OrbitIncDot		  0.0000000000000000e+00
            OrbitRAANDot		  0.0000000000000000e+00
            OrbitPerLongDot		  0.0000000000000000e+00
            OrbitMeanLongDot		  2.8516190899100002e+02

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		  1.5881739999999999e+05
        Radius		  7.8000000000000000e+03
        Magnitude		  0.0000000000000000e+00
        ReferenceDistance		  0.0000000000000000e+00

    END PhysicalData

    BEGIN AutoRename

        AutoRename		 Yes

    END AutoRename

    BEGIN Extensions

        BEGIN ExternData
        END ExternData

        BEGIN ADFFileData
        END ADFFileData

        BEGIN AccessConstraints
            LineOfSight IncludeIntervals

            UsePreferredMaxStep No
            PreferredMaxStep 360
        END AccessConstraints

        BEGIN Desc
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #7fff00
                LabelColor		 #7fff00
                LineColor		 #7fff00
                LineStyle		 0
                LineWidth		 1
                MarkerStyle		 2
                FontStyle		 0

            END Attributes

            BEGIN Graphics

                Show		 On
                Inherit		 Off
                ShowLabel		 On
                ShowPlanetPoint		 On
                ShowSubPlanetPoint		 Off
                ShowSubPlanetLabel		 Off
                ShowOrbit		 On
                NumOrbitPoints		 360
                OrbitTime		  1.0908674456827815e+05
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

