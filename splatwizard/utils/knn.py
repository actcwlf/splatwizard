from _cmod.simple_knn import distCUDA2
from _cmod.knn import knn_points, knn_gather

knn_dist = distCUDA2

__all__ = ['knn_dist', 'knn_points', 'knn_gather']